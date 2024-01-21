import json
import csv
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import os
import re


def get_time(line):
    time_string_temp=line[0:8]
    time_object_temp = datetime.strptime(time_string_temp, '%H:%M:%S')
    # get only time from datetime object
    time_object_temp = time_object_temp.time()
    return str(time_object_temp)


def get_mission_id(line):
    global mission_id_g
    if 'Start mission message received: ' in line:
        mission_id_string = line.split('Start mission message received: ', 1)[1]
        mission_json = json.loads(mission_id_string)
        mission_id_g = mission_json["mission"]["setMission"]["missionId"]


def get_pdb_json(line):
    pdb_json = None
    if 'Received JSON: {"pdb"' in line:
        pdb_json_string = line.split('Received JSON: ', 1)[1]
        pdb_json = json.loads(pdb_json_string)
    return pdb_json

# def get_value_of_key(line, key):
#     if key not in line:
#         return None
#     input_string = line.split(key+'":', 1)[1]
#     result = re.split(r',|}', input_string)
#     return result[0]

def get_value_of_key(input_string, substring):
    # Construct the regular expression pattern
    pattern = re.compile(f'{re.escape(substring)}\D*(\d+)')

    # Search for the pattern in the input string
    match = pattern.search(input_string)

    # If a match is found, return the captured number as an integer
    if match:
        return int(match.group(1))
    else:
        # Return None if no match is found
        return None

def create_lists(file_name, list_of_parameters):
    global mission_id_g
    global bat_type

    parameter_dict = {param: [] for param in list_of_parameters}
    parameter_dict["time"] = []
    parameter_dict["diff_consumed_mah_fg_vs_pdb_list"] = []
    with open(file_name, "r") as file:
        line_cnt = 0
        mission_id_g = "0"
        for line in file:
            line_cnt += 1
            try:
                get_mission_id(line)
            except KeyError:
                continue
            try:
                # find line that contails "PdbClient"
                if 'PdbClient' not in line:
                    continue

                for parameter in list_of_parameters:
                    if parameter in line:
                        value = get_value_of_key(line, parameter)
                        if value is not None:
                            parameter_dict[parameter].append(value)

                            # Add time
                            if parameter == list_of_parameters[0]:
                                parameter_dict["time"].append(get_time(line))


            except json.JSONDecodeError:
                pass

        for i in range (len(parameter_dict["av_cap"])):
            if parameter_dict["mah_consumed"][i] != 0:
                parameter_dict["diff_consumed_mah_fg_vs_pdb_list"].append((abs(parameter_dict["av_cap"][0] - parameter_dict["av_cap"][i]) / (parameter_dict["mah_consumed"][i]))*100)
            else:
                parameter_dict["diff_consumed_mah_fg_vs_pdb_list"].append(0)


    return parameter_dict

def create_csv_file(csv_filename, parameter_dict):
    #  create a rows for each of the keys in parameter_dict
    row = zip(*parameter_dict.values())
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(parameter_dict.keys())
        writer.writerows(row)

def create_plot(plot_filename , parameter_dict):

    minimum_len = get_mininum_list_len(parameter_dict)
    # make sure all lists are the same length
    for key in parameter_dict:
        parameter_dict[key] = parameter_dict[key][:minimum_len] # cut lists to minimum length



    fig, axs = plt.subplots(2, 2, figsize=(17, 10))

    plt.sca(axs[0, 0])
    plt.plot(parameter_dict["time"], parameter_dict["diff_consumed_mah_fg_vs_pdb_list"], label="Diff_consumed_mah_fg_vs_pdb")
    plt.xlabel("Time")
    x_ticks = np.arange(0, minimum_len, 15)
    plt.xticks(x_ticks)
    plt.ylim(75, 125)
    plt.gcf().autofmt_xdate()
    plt.legend()



    # plt.figure(figsize=(10, 6))
    # plt.subplot(121)
    plt.sca(axs[0, 1])
    plt.plot(parameter_dict["time"], parameter_dict["bat_charge_percent"], label="Bat Charge Percent")
    plt.plot(parameter_dict["time"], parameter_dict["av_soc"], label="av_soc")
    plt.xlabel("Time")
    x_ticks = np.arange(0, minimum_len, 15)
    plt.xticks(x_ticks)
    plt.gcf().autofmt_xdate()
    plt.legend()

    # plt.subplot(122)
    plt.sca(axs[1, 1])
    plt.plot(parameter_dict["time"], parameter_dict["mah_remain"], label="mah_remain")
    plt.plot(parameter_dict["time"], parameter_dict["av_cap"], label="av_cap")
    plt.xlabel("Time")
    x_ticks = np.arange(0, minimum_len, 15)
    plt.xticks(x_ticks)
    plt.gcf().autofmt_xdate()
    plt.legend()

    # plt.subplot(223)
    plt.sca(axs[1, 0])
    plt.plot(parameter_dict["time"], parameter_dict["last_mamps"], label="PDB amps")
    plt.plot(parameter_dict["time"], parameter_dict["system current[mA] "], label="FG amps")
    plt.xlabel("Time")
    x_ticks = np.arange(0, minimum_len, 15)
    plt.xticks(x_ticks)
    plt.gcf().autofmt_xdate()
    plt.legend()

    plt.savefig(plot_filename)
    # plt.show()

def get_mininum_list_len(dict):
    # get minmum length of all lists in dict
    minimum_len = 999999
    for key in dict:
        if len(dict[key]) < minimum_len:
            minimum_len = len(dict[key])
    return minimum_len


def main():

    global mission_id_g
    global bat_type
    list_of_parameters=["fg_temp", "system current[mA] ", "av_soc", "av_cap", "vcell[mv]", "bat_charge_percent", "bat_total_mah", "bat_type", "mah_remain", "last_mamps", "last_mvolts", "max_current", "mah_consumed", "mah_ltc4282"]
    dir_name = "logs"
    output_dir_name = "output"
    for filename in os.listdir(dir_name):
        full_filename = os.path.join(dir_name, filename)

        # Do something with the file here, for example:
        with open(full_filename, 'r') as fd:
            print("Processing file: {}".format(full_filename))
            try:
                parameter_dict = create_lists(full_filename, list_of_parameters)
                print(mission_id_g)
                # Check if vcell is above 3360
                if parameter_dict["vcell[mv]"] and np.mean(parameter_dict["vcell[mv]"]) > 3360 and np.max(parameter_dict["last_mamps"]) > 20000 :
                    if mission_id_g != 0:
                        full_output_file = os.path.join(output_dir_name, "{}_demo_{}".format(mission_id_g, filename))
                    else:
                        full_output_file = os.path.join(output_dir_name, filename)
                    print(full_output_file)
                    create_csv_file("{}.csv".format(full_output_file), parameter_dict)

                    create_plot("{}.png".format(full_output_file), parameter_dict)
                    # print("vcell:", vcell_list)
            except Exception as e:
                print(e)
                continue
            fd.close()
    print("Done")

if __name__ == '__main__':
    main()
