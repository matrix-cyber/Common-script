import socket
import random

def tcp_client(name, port):
    server_name = name
    server_port = port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    # sentence = input("Input lowercase sentence:")
    sentence = "aaa"
    client_socket.send(sentence.encode())
    modified_sentence = client_socket.recv(20000)
    print("From Server:", modified_sentence.decode())
    client_socket.close()

if __name__ == "__main__":
    name = "10.66.0.1"
    port = 80
    for i in range(0,10):
        tcp_client(name, port)