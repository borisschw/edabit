import time

class MyClass:
    def __init__(self):
        self.count = 0


    def recover_from_safety_charge(self):
        recovery_time_counter = 0
        self.counter += 1

        if recovery_time_counter == 0:
            print("0")
        elif (recovery_time_counter == 5):
            print("5")
        elif (recovery_time_counter == 10):
            print("10")

        print("recovery_time_counter = {}".format(recovery_time_counter))
        recovery_time_counter = self.recover_from_safety_charge.counter
        recovery_time_counter = self.counter
        if recovery_time_counter % (2 * 10) == 0:
            self.counter = 0

def main():
    my_class = MyClass()
    while(True):
        my_class.recover_from_safety_charge()
        time.sleep(1)


if __name__ == "__main__":
    main()