# valuse range is 0 - 1023(10 bit resolution)
# ref voltage is 0 - 5.00


#  need to map inputs 0 - 1023 into  0 - 5 V


def V_DAC(decimal_number):
    one_bit_voltage = 5 /1023
    return round(decimal_number * one_bit_voltage, 2)

print(V_DAC(400))
print(V_DAC(0))
print(V_DAC(1023))



