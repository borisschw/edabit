import json
import requests
import os
import copy
import threading
import zmq

from enum import Enum

class EventTypes(Enum):
    UNKNOWN = "base.unknown"
    ERROR   = "base.error"
    INFO    = "base.info"
    EVENT   = "base.event"

class PerfmonServer(threading.Thread):
    def __init__(self):

        self.data = {}
        self.AMPLITUDE_ENDPOINT = "https://api.amplitude.com/2/httpapi"

        # read key from file
        with open('key', 'r') as f:
            self.AMPLITUDE_API_KEY = f.read().strip()

        self.data['user_id'] =  os.environ.get('USER')
        self.data['platform'] = 'x86_64'
        self.data['version'] = 'N/A'
        self.data['user_properties'] = {
        }
        self.data['event_type'] = "base.unknown"
        self.data['event_properties'] = {
        }


    def __toDict(self, *args):
        # Ensure that the number of arguments is even (i.e., pairs)
        if len(*args) % 2 != 0:
            raise ValueError("You must pass an even number of arguments.")

        # Convert args to a dictionary by pairing elements
        it = iter(*args)
        result_dict = dict(zip(it, it))
        return result_dict
        # Convert the dictionary to a JSON string
        #return json.dumps(result_dict)

    def addUserProperty(self, *args):
        self.data['user_properties'] = self.__toDict(args)

    # Set properties for the next events
    def setProps(self, *args):
        # Ensure that the number of arguments is even (i.e., pairs)
        if len(args) % 2 != 0:
            raise ValueError("You must pass an even number of arguments.")
        self.data['event_properties'] = self.__toDict(args)


    def sendEvent(self, event_type, *event_properties):
        data= copy.deepcopy(self.data)

        # Ensure that the event type is valid
        if event_type not in (e.value for e in EventTypes):
            raise ValueError(f"Invalid event type {event_type}")

        data['event_type'] = event_type
        data['version'] = 'rc/2.96'
        data['event_properties'].update(self.__toDict(event_properties))

        try:
            self.__send_data(data)
        except Exception as e:
            print(f"Failed to send data: {e}")

    def __print_data(self, jsonData):
        print(jsonData)

    def __send_data(self, eventData):
        res = requests.post(self.AMPLITUDE_ENDPOINT, data=json.dumps({
            'api_key': self.AMPLITUDE_API_KEY,
            'events': [eventData],
        }))

        if res.status_code != 200:
            raise ValueError(f"Failed to send data: {res.text}")


perfmon = Perfmon()

perfmon.addUserProperty('serverName', 'drones.percepto.co',
                        'siteId', '1167')

perfmon.setProps('missionId', '115547',
                    'droneName', 'sparrow_32',
                    'charger type', 'powerlab',
                    'error', 'description of the error')

perfmon.sendEvent("base.error",
                  'error', 'description of the error',
                  'reason', 'reason of the error',
                  'wipers position', 'x: 23, y: 13, z: 6',)


perfmon.sendEvent("base.info",
                    'description', 'description of the info')







# # AMPLITUDE_API_KEY = "your-secret-amplitude-key"
# AMPLITUDE_ENDPOINT = "https://api.amplitude.com/2/httpapi"

# amp_event = {
#     "user_id": "base-qa9",       # device name
#     "event_type": "base.error",  # base.info, base.error, base.warning, etc.
#     "platform": 'x86_64',        # Architecture
#     "version": 'rc/2.96',        # version of the app
#     "user_properties": {
#         'serverName': 'drones.percepto.co',
#         'siteId': "1167"
#         # set any user-related info you want to tract and filter in Amplitude web UI
#     },
#     "event_properties": {
#         'missionId': '115547',
#         'droneName': 'sparrow_32',
#         'charger type': 'powerlab',
#         'stageId': '1',
#         'error': 'description of the error',
#         'wipers position': 'x: 0, y: 0, z: 0',
#         'battery level': '100%',
#         'temperature': '20C',
#         'dock status': 'true',
#         'docking count': '120',
#     },
# }

# # somehow we need to have json.dumps to make it works
# _ = requests.post(AMPLITUDE_ENDPOINT, data=json.dumps({
#     'api_key': AMPLITUDE_API_KEY,
#     'events': [amp_event],
# }))