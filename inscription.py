import socket
import json
import sys
import random
try:
    port=int(sys.argv[1])
except:
    port=(round(random.random()*10000))
    if port<100:
        port=port*100
    elif port<1000:
        port=port*10
    
with open('inscription.json', 'w') as mon_fichier:
    json.dump({'port':port}, mon_fichier)
Addressplayer = ('0.0.0.0', port)
serveraddress=('172.17.10.33',3000)
print(Addressplayer)
def inscription():
        print('test')
        with socket.socket() as s:
            s.connect(serveraddress)
            try:
                inscription={"request": "subscribe","port": port,"name":sys.argv[2],"matricules":["20004",sys.argv[3]]}
            except:
                inscription={"request": "subscribe","port": port,"name":'ptitbot{}'.format(random.random()),"matricules":["20004",str(random.random()*1000)]}
            message=json.dumps(inscription)
            s.send(message.encode())
            message=s.recv(2048).decode()
            print(message)
            if message=='{"response": "ok"}':
                print('OK ON COMMENCE')
            else:
                raise ValueError("Inscription Error: " + message)



