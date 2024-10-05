import network
import socket

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass

    print('Connected to WiFi')
    print('Network config:', wlan.ifconfig())

def send_data(data):
    # IP address and port of the receiver
    receiver_ip = '192.168.4.2'  # Replace with the IP address of the receiver
    receiver_port = 80  # Replace with the port number the receiver is listening on

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the receiver
        s.connect((receiver_ip, receiver_port))
        print("Connected to the receiver")

        # Send data
        s.sendall(data.encode())
        print("Data sent successfully")
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the socket
        s.close()

# Replace 'YOUR_WIFI_SSID' and 'YOUR_WIFI_PASSWORD' with your WiFi credentials
connect_to_wifi('myssid', 'mypassword')

# Example usage
data_to_send = "Hello, world!"
send_data(data_to_send)
