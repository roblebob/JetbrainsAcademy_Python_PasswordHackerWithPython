# write your code here
import sys
import socket

BUFFER_SIZE = 1024


def make_connection(ip, port, msg):
    with socket.socket() as client_socket:
        client_socket.connect((ip, port))
        client_socket.send(msg.encode())
        response = client_socket.recv(BUFFER_SIZE).decode()

    return response


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    msg = sys.argv[3]
    print(make_connection(ip, port, msg))