
import time
drone_info_time = time.time() - 5




def get_temp(input):
    if (input > 20):
        return None
    else:
        return input



def isDroneConnected(period = 20):
        print("drone_info_time = {}".format(drone_info_time))
        print("period = {}".format(period))
        print("Diff = {}".format(time.time() - drone_info_time))

        return time.time() - drone_info_time < period


def check_cond(cond1):
    if not cond1 and not isDroneConnected(60) and isDroneConnected(30*60):
        print("True")
    else:
        print("False")


# check_cond(False)



if get_temp(5) is None:
    print("None")
else:
    print("Not None")
