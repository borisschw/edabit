import re
def get_value_of_key(input_string, substring):
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



def get_mission_id(line):
    global mission_id_g
    if 'Start mission message received:' in line:
        get_value_of_key(line, "missionId")




get_mission_id(line)