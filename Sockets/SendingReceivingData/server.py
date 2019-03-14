import time
import pickle
import socket


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")

    sample_dict = {1: 'Hey', 2: 'There'}

    msg = pickle.dumps(sample_dict)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

    client_socket.send(msg)

    # while True:
    #     time.sleep(3)
    #     msg = f"The time is! {time.ctime()}"
    #     msg = f'{len(msg):<{HEADERSIZE}}' + msg
    #     client_socket.send(bytes(msg, 'utf-8'))
