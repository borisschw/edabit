import os, time
import json
import zmq


# ZMQ publish path
# TEMPS_ZMQ = os.getenv("ESC_ZMQ", "/tmp/temps")
TEMPS_ZMQ = os.getenv("TEMPS_ZMQ", "127.0.0.1:6666")

SENSOR_MAP = { 'gimbal' : 2, 'esc1' : 3, 'esc2' : 4, 'esc3' : 5, 'esc4' : 6, 'battery' : 7, 'board' : 8 }


def getSensorTelemetry(areaName):
    return { areaName:{'i':1, 't':2} }


def composeMessage():


    message = json.dumps( { 'temps' : { **getSensorTelemetry( 'gimbal' ),
                                        **getSensorTelemetry( 'battery' ),
                                        **getSensorTelemetry( 'board' )
                                        } }, sort_keys=True )
    return message


def main():

    # Create Zero-MQ socket for IPC
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://{}".format(TEMPS_ZMQ))
    msg = composeMessage().encode()
    while(1):
        socket.send(msg)
        time.sleep(0.1)


if __name__ == "__main__":
    main()


