import os, time
import zmq


# ZMQ publish path
TEMPS_ZMQ = os.getenv("ESC_ZMQ", "/tmp/temps")

def main():

    # Create Zero-MQ socket for IPC
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("ipc://{}".format(TEMPS_ZMQ))

    msg = "bla bla"
    while(1):
        socket.send(msg.encode())
        time.sleep(0.1)


if __name__ == "__main__":
    main()


