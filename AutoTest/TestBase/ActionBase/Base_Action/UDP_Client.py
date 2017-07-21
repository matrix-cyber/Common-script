import socket

def udp_client(ip,port):
    server_ip = ip
    server_port = port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "abc"
    client_socket.sendto(message.encode(), (server_ip, server_port)) #向UDP服务端发送报文
    # modified_message, server_address = client_socket.recvfrom(20000)
    # print(modified_message.decode())
    client_socket.close()

if __name__ == "__main__":
    ip = "10.66.0.1"
    port = 50000
    udp_client(ip,port)
    # for i in range(0,200):
    #     send_udp(ip,port)