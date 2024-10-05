import socket

# Define the server address and port
SERVER_ADDRESS = '192.168.4.1'
SERVER_PORT = 80

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

    # Send data to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode())
    print(f"Sent: {message}")

    # Receive data from the server
    data = client_socket.recv(1024)
    print("Received:", data.decode())

except Exception as e:
    print("Error:", e)

finally:
    # Close the socket
    client_socket.close()
