# write your code here
import sys
import socket
import string
import itertools
import requests

BUFFER_SIZE = 1024
MAX_NUM_PASSWORDS = 1_000_000
PASSWORDS_URL = "https://stepik.org/media/attachments/lesson/255258/passwords.txt"



def get_passwords_from_url(url):
    response = requests.get(url)
    return response.text.splitlines()

def variate_passwords(password):
    return set(map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in password))))



def generate_password(MAX):
    counter = 0
    for _password in get_passwords_from_url(PASSWORDS_URL):
        passwords = variate_passwords(_password)
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