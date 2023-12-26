
import re
ISDT_MINIMUM_OPERATING_TEMPERATURE = 0
ISDT_MAXIMUM_OPERATING_TEMPERATURE = 40

def __get_numeric_value(input_string):
    # matches either a float number (x.x) or decimat number or negative float number or negative decimal number
    match = re.search(r'(\d+\.\d+|\d+|\-\d+\.\d+|\-\d+)', input_string)
    if match:
        numeric_value = float(match.group())
        return numeric_value
    else:
        return -1

def main():
    print("Charger channel temperature is out of range [{} - {}] before starting charging".format(ISDT_MINIMUM_OPERATING_TEMPERATURE, ISDT_MAXIMUM_OPERATING_TEMPERATURE))
    input_string = "E0.5V"
    print(__get_numeric_value(input_string))
    input_string = "0.5.1"
    print(__get_numeric_value(input_string))

    input_string = "-5C"
    print(__get_numeric_value(input_string))

    input_string = "D-5.731dsfC"
    print(__get_numeric_value(input_string))

if __name__ == "__main__":
    main()