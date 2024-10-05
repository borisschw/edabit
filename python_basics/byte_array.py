# log raw data

raw_data = b'\x00' * 64
mutable_bytes = bytearray(raw_data)

rain_data_mm_h = 356.87
rain_data_val = int(rain_data_mm_h * 100 / 25.4)

# get the low byte of rain_data_val
rain_data_val_low = rain_data_val & 0xFF

# get the high byte of rain_data_val
rain_data_val_high = (rain_data_val >> 8) & 0xFF

# Update values at indices 40 and 41
mutable_bytes[41:43] = [rain_data_val_low, rain_data_val_high]
raw_data = bytes(mutable_bytes)

self.logger.debug(list(raw_data))
