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