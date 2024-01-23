# write your code here
import sys
import socket
import string
import itertools

BUFFER_SIZE = 1024
MAX_NUM_PASSWORDS = 1_000_000


def generate_password(MAX):
    chars = list(string.ascii_lowercase + string.digits)
    length = 1
    counter = 0
    while counter < MAX:
        passwords = list(map(lambda s: ''.join(s), itertools.product(chars, repeat=length)))
        length += 1
        for password in passwords:
            yield password
            counter += 1
            if counter == MAX:
                break


def make_connection(ip, port):
    with socket.socket() as client_socket:
        client_socket.connect((ip, port))
        for password in generate_password(MAX_NUM_PASSWORDS):
            client_socket.send(password.encode())
            response = client_socket.recv(BUFFER_SIZE).decode()
            if response == "Connection success!":
                return password

    return None


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    print(make_connection(ip, port))