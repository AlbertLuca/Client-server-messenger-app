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

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Start a thread to send messages
send_thread = threading.Thread(target=send_message, args=(client_socket,))
send_thread.start()

# Recieve and display messages from the server
while True:
    data = client_socket.recv(1024)
    if not data:
        break

    print(data.decode())

client_socket.close()