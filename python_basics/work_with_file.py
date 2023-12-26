

import os

TEMPERATURE_SIM_PATH = "/home/boris/myProjects/python_practice/isdt_temp.txt"

def get_temperature():
    if os.path.exists(TEMPERATURE_SIM_PATH):
        with open(TEMPERATURE_SIM_PATH, 'r') as f:
            try:
                file_temp = float(f.readline())
                # print("ISDT getting simulated temperature from file: {}".format(file_temp))
                return file_temp
            except:
                print("ISDT failed to parse temperature from file, returning real value")
    return 0



print(get_temperature())