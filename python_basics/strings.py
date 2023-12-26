def __get_error_code(errorx):
    if errorx is None:
        print("ISDT Charger errorx is None")
        return "Null"
    # res = errorx.split(' ')
    res = str(errorx).split('\n\r', 1)[0]
    if len(res) < 2:
        print("ISDT Charger error parsing error code")
        return "Null"

    # error = res[1:].split('\n\r', 1)[0]
    error = res.split(' ', 1)[1]
    return error




print(__get_error_code("@errorx InputVoltage dfg fgfd\n\r"))