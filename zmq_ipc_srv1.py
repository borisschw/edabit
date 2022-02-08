import os, time
import zmq

# TMEPS publish path
TEMPS_ZMQ = os.getenv("ESC_ZMQ", "/tmp/temps")


def main():
    # Create Zero-MQ socket for IPC
    context = zmq.Context()
    temps_socket = context.socket(zmq.SUB)
    # Set socket to keep only last message in queue
    temps_socket.setsockopt(zmq.CONFLATE, 1)
    temps_socket.connect("ipc://{}".format(TEMPS_ZMQ))
    # Subscribe to any
    temps_socket.subscribe("")

    while(1):
        try:
            tmp_telemetry = temps_socket.recv(zmq.NOBLOCK)
        except zmq.error.Again:
            tmp_telemetry = None

        time.sleep(0.5)
        print("This is server 1")
        print(tmp_telemetry)



if __name__ == "__main__":
    main()