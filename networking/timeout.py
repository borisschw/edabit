import logging.config
import time
import json
import socket
import logging
import os

# Logger settings:
LOGGING = {
  "version": 1,
  "disable_existing_loggers": False,
  "formatters": {
    "detailed": {
      "class": "logging.Formatter",
      "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    }
  },
  "handlers": {
    "syslog": {
      "class": "logging.handlers.SysLogHandler",
      "formatter": "detailed",
      "address": "/dev/log"
    }
  },
  "loggers": {
    "": {
      "handlers": ["syslog"],
      "level": "DEBUG"
    }
  }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger("charger_wd")


logger.info("Charger Watchdog started")

# Get timeout in seconds from the environment
timeout_sec = os.getenv("TIMEOUT", "4")
try:
    timeout_sec = int(timeout_sec)
except Exception as e:
    logger.error("Error while converting timeout_sec to int: " + str(e))
    exit(-1)

# Get gpio number from the environment
GPIO_NUMBER = os.getenv("GPIO_NUMBER", "0")
try:
    GPIO_NUMBER = int(GPIO_NUMBER)
except Exception as e:
    logger.error("Error while converting GPIO_NUMBER to int: " + str(e))
    exit(-1)

# Get to polatiry from the environment (normal/inverted)
POLARITY = os.getenv("POLARITY", "normal")

#Get the ip address from the environment
LOCAL_IP = os.getenv("IP", "localhost")

# Get the port number from the environment
GPIO_CONTROL_PORT = os.getenv("GPIO_PORT", "2382")
try:
    GPIO_CONTROL_PORT = int(GPIO_CONTROL_PORT)
except Exception as e:
    logger.error("Error while converting GPIO_CONTROL_PORT to int: " + str(e))
    exit(-1)


# Get the DOCKER_CONTROL_PORT from the environment
DOCKER_CONTROL_PORT = os.getenv("DOCKER_PORT", "2370")
try:
    DOCKER_CONTROL_PORT = int(DOCKER_CONTROL_PORT)
except Exception as e:
    logger.error("Error while converting DOCKER_CONTROL_PORT to int: " + str(e))
    exit(-1)


def charger_enable(enable):

    if enable:
        gpio_val = 1 if POLARITY == "normal" else 0
    else:
        gpio_val = 0 if POLARITY == "normal" else 1

    try:
        gpio_control_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except Exception as e:
        logger.error("Error while creating socket: " + str(e))
        return

    try:
        message = json.dumps({"op":"set","io":GPIO_NUMBER,"value":gpio_val})
        gpio_control_socket.sendto(message.encode(), (LOCAL_IP, GPIO_CONTROL_PORT))
    except Exception as e:
        logger.error("Error while processing control message: " + str(e))
    finally:
        logger.debug("Closing socket")
        gpio_control_socket.close()


# This serveice should wait for a ping from the charger
# In case recieved the ping 5 times in a row, send a command to the GPIO server to start the charger
# in case the ping was not recieved for 5 seconds, send a command to the GPIO server to stop the charger

def main():
    # Create a socket to listen for local control messages
    docker_control_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    docker_control_socket.bind((LOCAL_IP, DOCKER_CONTROL_PORT))
    docker_control_socket.settimeout(timeout_sec)

    msg_counter = 0

    while True:
        try:
          # Listen for control messages
            data, addr = docker_control_socket.recvfrom(1024)

            logger.debug("Received control message: {}". format(data))

            # Parse control message
            message = json.loads(data)
            logger.debug("Parsed control message: " + str(message))

            # Message is json that looks like {"charger": "ping"}
            operation_type = message["charger"]
            if operation_type == "ping":
                msg_counter += 1
                if msg_counter == 5:
                    logger.debug("Send command to GPIO server to start the charger")
                    charger_enable(True)
                    msg_counter = 0


        except socket.timeout:
            charger_enable(False)
            msg_counter = 0
            logger.debug("Timeout reached. No control message received.")

        except Exception as e:
            logger.error("Error while processing control message: " + str(e))
            exit(-1)
            # Send a command to the GPIO server

if __name__ == "__main__":
    main()