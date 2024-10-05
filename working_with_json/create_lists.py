import json
import csv
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import os

# Initialize empty lists for each value
pdb_time_list = []
bat_charge_percent_list = []
# battery_pct_under_test_list = []
bat_conumed_mah_list = []
fg_temp_list = []
system_currentmA_list = []
av_soc_list = []
mah_remain_list = []
av_cap_list = []
last_mamps_list = []
last_mvolts_list = []
max_current_list = []
mah_consumed_list = []
mah_ltc4282_list = []
vcell_list = []
mission_id_g = 0
bat_type = 0

def clear_lists():
    global mission_id_g
    global bat_type
    pdb_time_list.clear()
    bat_charge_percent_list.clear()
    # battery_pct_under_test_list.clear()
    bat_conumed_mah_list.clear()
    fg_temp_list.clear()
    system_currentmA_list.clear()
    av_soc_list.clear()
    mah_remain_list.clear()
    av_cap_list.clear()
    last_mamps_list.clear()
    last_mvolts_list.clear()
    max_current_list.clear()
    mah_consumed_list.clear()
    mah_ltc4282_list.clear()
    vcell_list.clear()
    mission_id_g = 0
    bat_type = 0


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


def create_lists(file_name):
    global mission_id_g
    global bat_type
    with open(file_name, "r") as file:
        for line in file:
            try:
                get_mission_id(line)
            except KeyError:
                continue

            try:
                data = get_pdb_json(line)
                if (data != None):


                    try:
                        fg_temp = data["pdb"]["Balancer_info"]["fg_temp"]
                        fg_temp_list.append(fg_temp)

                        system_currentmA = data["pdb"]["Balancer_info"]["system current[mA] "]
                        system_currentmA_list.append(system_currentmA)

                        av_soc = data["pdb"]["Balancer_info"]["av_soc"]
                        av_soc_list.append(av_soc)

                        av_cap = data["pdb"]["Balancer_info"]["av_cap"]
                        av_cap_list.append(av_cap)

                        vcell = data["pdb"]["Balancer_info"]["vcell[mv]"]
                        vcell_list.append(vcell)


                    except KeyError:
                        continue

                    bat_charge_percent = data["pdb"]["battery"]["bat_charge_percent"]
                    bat_charge_percent_list.append(bat_charge_percent)

                    bat_charge_percent = data["pdb"]["battery"]["bat_total_mah"]
                    bat_conumed_mah_list.append(bat_charge_percent)

                    bat_type = data["pdb"]["battery"]["bat_type"]

                    # battery_pct_under_test = data["pdb"]["battery"]["battery_pct_under_test"]
                    # battery_pct_under_test_list.append(battery_pct_under_test)

                    pdb_time_list.append(get_time(line))

                    mah_remain = data["pdb"]["mah_remain"]
                    mah_remain_list.append(mah_remain)

                    last_mamps = data["pdb"]["last_mamps"][9]
                    last_mamps_list.append(last_mamps)

                    last_mvolts = data["pdb"]["last_mvolts"][9]
                    last_mvolts_list.append(last_mvolts)

                    max_current = data["pdb"]["max_current"]
                    max_current_list.append(max_current)

                    mah_consumed = data["pdb"]["mah_consumed"]
                    mah_consumed_list.append(mah_consumed)

                    mah_ltc4282 = data["pdb"]["mah_ltc4282"]
                    mah_ltc4282_list.append(mah_ltc4282)


            except json.JSONDecodeError:
                pass

    return 0

def create_csv_file(csv_filename):
    rows = zip(pdb_time_list, bat_charge_percent_list,bat_conumed_mah_list,
            fg_temp_list, system_currentmA_list, av_soc_list, mah_remain_list,vcell_list,
            av_cap_list, last_mamps_list, last_mvolts_list, max_current_list,
            mah_consumed_list, mah_ltc4282_list)
    # print(rows)
    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Time", "Bat Charge Percent","Bat Consumed Mah",
                                "FG Temp", "System Current(mA)", "AV SOC", "Mah Remain","VCell",
                                "AV Cap", "Last mamps", "Last mvolts", "Max Current",
                                "Mah Consumed", "Mah LTC4282"])
        csv_writer.writerows(rows)

def create_plot(plot_filename):


    plt.figure(figsize=(10, 6))
    plt.subplot(121)

    plt.plot(pdb_time_list, bat_charge_percent_list, label="Bat Charge Percent")
    plt.plot(pdb_time_list, av_soc_list, label="av_soc")
    plt.xlabel("Time")
    x_ticks = np.arange(0, len(pdb_time_list), 15)
    plt.xticks(x_ticks)
    plt.gcf().autofmt_xdate()
    plt.legend()

    plt.subplot(122)
    plt.plot(pdb_time_list, mah_remain_list, label="mah_remain")
    plt.plot(pdb_time_list, av_cap_list, label="av_cap")
    plt.xlabel("Time")
    x_ticks = np.arange(0, len(pdb_time_list), 15)
    plt.xticks(x_ticks)
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.savefig(plot_filename)
    # plt.show()

def main():
    global mission_id_g
    global bat_type
    dir_name = "logs"
    output_dir_name = "output"
    for filename in os.listdir(dir_name):
            full_filename = os.path.join(dir_name, filename)

            # Do something with the file here, for example:
            with open(full_filename, 'r') as fd:
                print("Processing file: {}".format(full_filename))
                if (create_lists(full_filename) == 0):
                    print(mission_id_g)
                    # if bat_type is not 0 and average vcell is above 3360
                    if bat_type != 0 and np.mean(vcell_list) > 3360:
                        if mission_id_g != 0:
                            full_output_file = os.path.join(output_dir_name, "{}_demo_{}".format(mission_id_g, filename))
                        else:
                            full_output_file = os.path.join(output_dir_name, filename)
                        print(full_output_file)

                        create_csv_file("{}.csv".format(full_output_file))
                        create_plot("{}.png".format(full_output_file))
                        # print("vcell:", vcell_list)
                clear_lists()
                fd.close()


if __name__ == '__main__':
    main()
