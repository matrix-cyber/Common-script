import socket
import socketserver
import time
import threading

def tcp_server(port):
    server_port = port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("The server is ready to receive")
    while 1:
        connetcion_socket,addr = server_socket.accept()
        sentence = connetcion_socket.recv(20000)
        capitalized_sentence = sentence.upper()
        connetcion_socket.send(capitalized_sentence)
        connetcion_socket.close()

if __name__ == "__main__":
    port = 50001
    tcp_server(port)