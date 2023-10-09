import socket
import threading

# Define the server's host and port
server_host = '127.0.0.1'  # Replace with the server's IP address if not on localhost
server_port = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((server_host, server_port))

# Listen for incoming connections (maximum 5 clients in the queue)
server_socket.listen(5)

print(f"Server is listening on {server_host}:{server_port}")

# List to store connected client sockets
connected_clients = []

# Function to handle a client's connection
def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')

            if not data:
                # If no data received, the client may have disconnected
                print(f"Client disconnected.")
                break

            print(f"Received data from {client_socket.getpeername()}: {data}")

            # Echo the received data back to the client
            client_socket.send(data.encode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Remove the client from the list of connected clients and close the socket
        connected_clients.remove(client_socket)
        client_socket.close()

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Add the client socket to the list of connected clients
    connected_clients.append(client_socket)

    # Start a new thread to handle the client's connection
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
