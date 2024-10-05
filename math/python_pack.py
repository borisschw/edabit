from struct import pack, unpack



def write_register(addr, register, data, reg_bytes = 1, reg_byteorder = 'big'):
        """ Generic write to a specific register, position or command. See description in I2C_Slave class. """

        if type(data) == int:
            data = bytes([data])
        elif type(data) == list:
            data = bytes(data)

        print("data:{}".format(data))

        print("Want to write: addr:{}, data:{}".format(addr, register.to_bytes(reg_bytes, byteorder=reg_byteorder) + data))


def write_word_data(i2c_addr, register, value, force=None):
        """
        Write a single word (2 bytes) to a given register.

        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Register to write to
        :type register: int
        :param value: Word value to transmit
        :type value: int
        :param force:
        :type force: Boolean
        :rtype: None
        """
        data = pack("h", value)
        print(data)
        write_register(i2c_addr, register, data)





# Hexadecimal value
hex_value = 0x8050

# Pack the value as an unsigned short (16-bit)
packed_data = pack('H', hex_value)

print("packed data: {}" .format(packed_data))

# Unpack the value as a signed short (16-bit)
dataToSend = unpack('h', packed_data)[0]

print("unpacked data: {}" .format(dataToSend))

# conver dataToSend to unsigned short
dataToSend = dataToSend & 0xffff


#write_word_data(0x47, 0x46, dataToSend)



