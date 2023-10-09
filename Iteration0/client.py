import socket

# Define the server's host and port
server_host = '127.0.0.1'  # Replace with the server's IP address if not on localhost
server_port = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Send a message to the server
message = "Hello, Server!"
client_socket.send(message.encode('utf-8'))

# Receive and display the echoed message from the server
received_data = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {received_data}")

# Close the client socket
client_socket.close()
