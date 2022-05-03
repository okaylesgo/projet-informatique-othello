import socket
import asyncio
import json
import sys
from xml.etree.ElementInclude import include

from scipy import rand
try:
    port=int(sys.argv[1])
except:
    port=3333
    Addressplayer = ('0.0.0.0', port)
    serveraddress=('localhost',3000)
    def inscription():
            print('test')
            with socket.socket() as s:
                s.connect(serveraddress)
                try:
                    inscription={"request": "subscribe","port": port,"name":sys.argv[2],"matricules":["20004",sys.argv[3]]}
                except:
                    inscription={"request": "subscribe","port": port,"name":'ptitbot{}'.format(rand()),"matricules":["20004",str(rand()*1000)]}
                message=json.dumps(inscription)
                s.send(message.encode())
                message=s.recv(2048).decode()
                print(message)
                if message=='{"response": "ok"}':
                    print('OK ON COMMENCE')
                else:
                    raise ValueError("Inscription Error: " + message)



