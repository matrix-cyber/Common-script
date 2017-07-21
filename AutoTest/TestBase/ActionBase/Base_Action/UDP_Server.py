import socket

def udp_server(port):
    server_port = port
    server_socke = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socke.bind(('', server_port)) #UDP服务端监听端口
    print("The server is ready to receive")
    while 1:
        messag, clientAddress = server_socke.recvfrom(20000)
        modified_message = messag.upper()
        # modified_message = messag.lower()
        server_socke.sendto(modified_message, clientAddress)

if __name__ == "__main__":
    port = 60005
    udp_server(port)
