

import numpy as np
VOUT_N = -9

# def twos_comp(val, bits):
#     #compute the 2's complement of int value val
#     if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
#         val = val - (1 << bits)        # compute negative value
#     return val


# def _decodePMBus(message):
#     # print("Got message", bin(message))
#     messageN = message >> 11
#     # print("messageN = ", messageN)
#     messageY = message & 0b0000011111111111
#     # print("messageY = ", messageY)
#     message = messageY*(2.0**(twos_comp(messageN, 5))) #calculate real values (everything but VOUT works)
#     # print("decoded message", message)
#     return message


def getVoltageOut(voltageOutMessage):
    voltageOut = voltageOutMessage*(2.0**VOUT_N)
    return voltageOut


#test the getVoltageOut function

#loop with intervals of 0.1
for i in np.arange(0, 2**16-1, 0.01):
    # print("i = ", i)

    if (getVoltageOut(i) > 128):
        print("Voltage out is greater")
        print("Voltage out is: ", getVoltageOut(i/10))



