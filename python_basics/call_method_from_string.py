class Device:
    def __init__(self):
        self.__charging_target = None
        self.__battery_percentage = None
        self.__is_on = False

    def __handle_cmd(self, cmd):

        command = cmd.get("cmd")
        params = cmd.get("params", {})

        if command == "set_charging_target":
            charging_target_pct = params.get("charging_target_pct")
            batt_type = params.get("batt_type")
            if charging_target_pct is not None and batt_type is not None:
                if (self.__set_charging_target(charging_target_pct, batt_type)):
                    self.send_ping()
            else:
                print(f"Missing parameters for command: {command}")

        elif command == "set_battery_percentage":
            percent = params.get("percent")
            batt_type = params.get("batt_type")
            if percent is not None and batt_type is not None:
                if (self.__set_battery_percentage(percent, batt_type)):
                    self.__turn_on()
                    self.send_ping()
            else:
                print(f"Missing parameters for command: {command}")

        elif command == "start_charge":
            self.__start_charge()
            self.send_ping()

        elif command == "turn_on":
            self.__turn_on()
            self.send_ping()

        elif command == "turn_off":
            if (self.__turn_off()):
                self.send_ping()

        elif command == "reset":
            self.__reset()

        else:
            print("Unknown command: " + str(cmd))

    def handle_cmd(self, cmd):
        self.__handle_cmd(cmd)

    def __set_charging_target(self, charging_target_pct, batt_type):
        # Simulate setting the charging target
        print(f"Setting charging target to {charging_target_pct}% for battery type {batt_type}")
        self.__charging_target = charging_target_pct
        return True  # Simulated success

    def __set_battery_percentage(self, percent, batt_type):
        # Simulate setting battery percentage
        print(f"Setting battery percentage to {percent}% for battery type {batt_type}")
        self.__battery_percentage = percent
        return True  # Simulated success

    def __start_charge(self):
        # Simulate starting charging
        print("Starting charging")
        return True  # Simulated success

    def __turn_on(self):
        # Simulate turning on
        print("Turning on")
        self.__is_on = True
        return True  # Simulated success

    def __turn_off(self):
        # Simulate turning off
        print("Turning off")
        self.__is_on = False
        return True  # Simulated success

    def __reset(self):
        # Simulate resetting
        print("Resetting")
        self.__charging_target = None
        self.__battery_percentage = None
        self.__is_on = False

    def send_ping(self):
        # Simulate sending a ping
        print("Sending ping")


# Testing the handle_cmd method with simulated commands
if __name__ == "__main__":
    device = Device()

    # Simulating a valid set_charging_target command
    cmd1 = {"cmd": "set_charging_target", "params": {"charging_target_pct": 80, "batt_type": "Li-ion"}}
    device.handle_cmd(cmd1)

    # Simulating a valid set_battery_percentage command
    cmd2 = {"cmd": "set_battery_percentage", "params": {"percent": 50, "batt_type": "Li-ion"}}
    device.handle_cmd(cmd2)

    # Simulating a valid start_charge command
    cmd3 = {"cmd": "start_charge"}
    device.handle_cmd(cmd3)

    # Simulating a valid turn_on command
    cmd4 = {"cmd": "turn_on"}
    device.handle_cmd(cmd4)

    # Simulating a valid turn_off command
    cmd5 = {"cmd": "turn_off"}
    device.handle_cmd(cmd5)

    # Simulating a valid reset command
    cmd6 = {"cmd": "reset"}
    device.handle_cmd(cmd6)

    # # Simulating an unknown command
    # cmd7 = {"cmd": "unknown_command"}
    # device.handle_cmd(cmd7)

    # # Simulating missing parameters for set_charging_target
    # cmd8 = {"cmd": "set_charging_target", "params": {"charging_target_pct": 90}}
    # device.handle_cmd(cmd8)

    # # Simulating missing parameters for set_battery_percentage
    # cmd9 = {"cmd": "set_battery_percentage", "params": {"batt_type": "Li-ion"}}
    # device.handle_cmd(cmd9)
