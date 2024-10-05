
import json
import subprocess

def create_device_list(dev_list):
    device_dict = {}
    endpoint_cnt = 0
    for line in dev_list:
        if "Bus" in line and "Device" in line and "ID" in line:
            device_name = line
            device_dict[device_name] = 0
            endpoint_cnt = 0
        if "bNumEndpoints" in line:
            endpoint_cnt = int(line.split()[1])
            device_dict[device_name] += endpoint_cnt

    print(json.dumps(device_dict, indent=4))
    print("Total number of used endpoints: ", sum(device_dict.values()))

def get_device_list():
    command = "lsusb -v"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    dev_list = output.decode("utf-8")

    return dev_list



dev_list = get_device_list()

create_device_list(dev_list.split("\n"))
