import socket 
import threading 
import os

# Client Configuration
HOST = 'localhost'
PORT = 12345

def send_message(client_socket):
    while True:
        message = input()
        if message.lower() == 'exit':
            break

        if os.path.isfile(message):
            # Send a file
            client_socket.send(f'FILE:{message}'.encode())
            with open(message, 'rb') as file:
                file_data = file.read(1024)
                while file_data:
                    client_socket.send(file_data)
                    file_data = file.read(1024)

        else:
            # Send a message
            client_socket.send(message.encode())