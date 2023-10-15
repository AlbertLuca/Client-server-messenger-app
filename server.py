import socket 
import threading 
import os

# Client Configuration
HOST = 'localhost'
PORT = 12345

# Create a socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

# Function to habndle a client
def handle_client(client_socket):
    with client_socket as sock:
        print(f"New connection from {client_socket.getpeername()}")
        clients.append(sock)

        while True:
            try:
                data = sock,recv(1024)
                if not data:
                    break

                # Broadcast the recieved message to all clients
                for client in clients:
                    if client != sock:
                        client.send(data)

                # Check if the message is a file
                if data.startswith(b'FILE:'):
                    file_name = data[5:].decode()
                    file_data = sock.recv(1024)
                    with open(file_name, 'wb') as file:
                        file.write(file_data)
                        print(f"File {file_name} recieved successfully")
            

            except Exception as e:
                print(f"Exception: {e}")
                break

        print(f"Connection from {client_socket.getpeername()} closed")
        client.remove(sock)

# Listen for incoming connections
print(f"Listening for connections on {HOST}:{PORT}...")