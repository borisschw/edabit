
import re
ISDT_MINIMUM_OPERATING_TEMPERATURE = 0
ISDT_MAXIMUM_OPERATING_TEMPERATURE = 40


get_numeric_value = lambda s: float(''.join(filter(lambda c: c.isdigit() or c == "-" or c == ".", s)))


# def __get_cell_voltages(cvx):
#     cells_array = [0,0,0,0,0,0]
#     if cvx is None:
#         print("ISDT Charger cell voltages is None")
#         return cells_array
#     res = cvx.split(' ')
#     cells_string = res[2:-1]
#     for i in range (0, len(cells_string)):
#         clean_val = cells_string[i].replace(".", "", 1)
#         if (clean_val.isnumeric()):
#             cells_array[i] = float(get_numeric_value(cells_string[i]))
#         else:
#             print("cells string contains non-numeric values")
#             print(cells_string)
#             break
#     return cells_array


def __get_cell_voltages(cvx):
    cells_array = [0,0,0,0,0,0]
    if cvx is None:
        print("ISDT Charger cell voltages is None")
        return cells_array
    res = cvx.split(' ')
    cells_string = res[2:-1]
    for i in range (0, len(cells_string)):
        clean_val = cells_string[i].replace(".", "", 1)
        if (clean_val.isdigit()):
            cells_array[i] = float(cells_string[i])
        else:
            print("ISDT Charger cell voltages contains non-numeric values")
            print(cells_string)
    return cells_array




def __get_numeric_value(input_string):
    # matches either a float number (x.x) or decimat number or negative float number or negative decimal number
    match = re.search(r'(\d+\.\d+|\d+|\-\d+\.\d+|\-\d+)', input_string)
    if match:
        numeric_value = float(match.group())
        return numeric_value
    else:
        return -1

def main():
    # print("Charger channel temperature is out of range [{} - {}] before starting charging".format(ISDT_MINIMUM_OPERATING_TEMPERATURE, ISDT_MAXIMUM_OPERATING_TEMPERATURE))
    input_string = "E0.5V"

    # print(get_numeric_value(input_string))


    print(__get_cell_voltages("@ cvx 3.85 3.81 4s 3.86 3.96 5s \n\r"))

    # print(__get_numeric_value(input_string))
    # input_string = "0.5.1"
    # print(__get_numeric_value(input_string))

    # input_string = "-5C"
    # print(__get_numeric_value(input_string))

    # input_string = "D-5.731dsfC"
    # print(__get_numeric_value(input_string))

if __name__ == "__main__":
    main()