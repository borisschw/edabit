def read_data(max_length, min_length=0):
    try:
        rbuf = [1,2,3,4,5]
        # Check that the rbuf length is above 23
        if len(rbuf) <= min_length:
            raise Exception("rbuf length is less than {}".format(min_length))
    except Exception as e:
        print("I2C Init read failed: {}".format(e))
        return -1
    return rbuf




x =  -1 if (rbuf := read_data(65, 4)) == -1 else rbuf
print(x)

if (x == -1 or x[1] == 0x00):
    print("Error")
else:
    print("Success")



