
sensor_map = { 'gimbal' : [2,0], 'esc1' : 3, 'esc2' : 4, 'esc3' : 5, 'esc4' : 6, 'battery' : 7, 'board' : 8 }

sensor_map_1 = { 'power interface' : 1, 'core' : 2, 'battery' : [1,4] }


cmd = {"cmd": "command", "params": {"param_name1": 1, "param_name2": 2, "param_name3": 3}}

cmd.get("cmd_name")
cmd.keys.__annotations_
# get cmd name:
cmd_name = list(cmd.keys())[0]
