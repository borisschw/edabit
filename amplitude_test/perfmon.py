import zmq
import json

class Perfmon():
    def __init__(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.PUSH)
        self.socket.connect("tcp://localhost:5555")  # Connect to the server



    def sendEvent(self, event_type, *event_properties):
        data = {}
        data['event_type'] = event_type
        data['event_properties'] = event_properties
        self.socket.send_string(json.dumps(data))

