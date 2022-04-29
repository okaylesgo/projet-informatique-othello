import socket
import asyncio
import json
import sys
port=int(sys.argv[1])
Addressplayer = ('0.0.0.0', port)
serveraddress=('localhost',3000)
def inscription():
        print('test')
        with socket.socket() as s:
            s.connect(serveraddress)
            inscription={"request": "subscribe","port": port,"name":sys.argv[2],"matricules":["20004",sys.argv[3]]}
            message=json.dumps(inscription)
            s.send(message.encode())
            message=s.recv(2048).decode()
            print(message)
            if message=='{"response": "ok"}':
                print('OK ON COMMENCE')
            else:
                raise ValueError("Inscription Error: " + message)
if __name__ == '__main__':
    inscription()


