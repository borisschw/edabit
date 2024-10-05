# import re


# def get_value_of_key(line, key):
#     if key not in line:
#         return None
#     input_string = line.split(key, 1)[1]
#     print(input_string)
#     input_string = re.split('":|":["', input_string)
#     print(input_string)
#     return None
#     result = re.split(r',|}', input_string)
#     return result[0]


import re

def get_next_number_after_substring(input_string, substring):
    # Construct the regular expression pattern
    pattern = re.compile(f'{re.escape(substring)}\D*(\d+)')

    # Search for the pattern in the input string
    match = pattern.search(input_string)

    # If a match is found, return the captured number as an integer
    if match:
        return int(match.group(1))
    else:
        # Return None if no match is found
        return None

# Example usage:
input_string = '18:12:55.917	PdbClient   	DEBUG	[MSG] Received JSON: {"pdb":{"battery":{"bat_id":"00000de4193a","bat_type":2,"battery_pct_under_test":49,"bat_usable":true,"bat_total_mah":735662,"bat_charge_percent":49,"bat_total_cons_pst":40,"bat_was_below_20":false,"bat_eeprom_write_cnt":6491,"is_charging":false},"Balancer_info":{"bal_temp[mC]":0,"voltage[mV]":0,"battery_pct[mili %]":0,"cells[mV]":[0,0,0,0,0,0],"cells_delta[mV]":0,"is_balancer_active":false,"is_battery_charged":false,"docking status  ":0,"fg_temp":21,"system current[mA] ":-1406,"vcell[mv]":3806,"av_soc":48,"av_cap":15749,"bal_time[sec]":[0,0,0,0,0,0],"profile":[100,60,40,300],"target":"Full"},"5v_mamps":1058,"5v_mvolts":5001,"last_mamps":[1660,1562,1562,1464,1367,1464,1464,1367,1367,1367],"last_mvolts":[22912,22912,22912,22912,22912,22912,22912,22920,22912,22912],"12v_mvolts":[11998,11998,11998,11998,11998,11998,11998,11998,11997,11997],"12v_mamps":[568,568,566,566,569,569,571,571,574,574],"time_left_min":0,"temp_cpu":22500,"temp_gpu":17000,"low_voltage":false,"high_voltage":false,"max_current":1660,"mah_consumed":5,"mah_remain":11859,"mah_ltc4282":3,"status":"success"}}'
substring = 'battery_pct_under_test'

next_number = get_next_number_after_substring(input_string, substring)

if next_number is not None:
    print(f'The next number after "{substring}" is: {next_number}')
else:
    print(f'No number found after "{substring}"')



# line = '18:12:55.917	PdbClient   	DEBUG	[MSG] Received JSON: {"pdb":{"battery":{"bat_id":"00000de4193a","bat_type":2,"battery_pct_under_test":49,"bat_usable":true,"bat_total_mah":735662,"bat_charge_percent":49,"bat_total_cons_pst":40,"bat_was_below_20":false,"bat_eeprom_write_cnt":6491,"is_charging":false},"Balancer_info":{"bal_temp[mC]":0,"voltage[mV]":0,"battery_pct[mili %]":0,"cells[mV]":[0,0,0,0,0,0],"cells_delta[mV]":0,"is_balancer_active":false,"is_battery_charged":false,"docking status  ":0,"fg_temp":21,"system current[mA] ":-1406,"vcell[mv]":3806,"av_soc":48,"av_cap":15749,"bal_time[sec]":[0,0,0,0,0,0],"profile":[100,60,40,300],"target":"Full"},"5v_mamps":1058,"5v_mvolts":5001,"last_mamps":[1660,1562,1562,1464,1367,1464,1464,1367,1367,1367],"last_mvolts":[22912,22912,22912,22912,22912,22912,22912,22920,22912,22912],"12v_mvolts":[11998,11998,11998,11998,11998,11998,11998,11998,11997,11997],"12v_mamps":[568,568,566,566,569,569,571,571,574,574],"time_left_min":0,"temp_cpu":22500,"temp_gpu":17000,"low_voltage":false,"high_voltage":false,"max_current":1660,"mah_consumed":5,"mah_remain":11859,"mah_ltc4282":3,"status":"success"}}'

# val = get_value_of_key(line, 'last_mamps')

# print(val)


# # val = get_value_of_key(line, 'battery_pct_under_test')

# # print(val)