import socket
import asyncio
import json
from IA import IA
from IA2 import IA2
import sys
from message import quelmessagejenvoie
with open('inscription.json') as mon_fichier:
    d=json.load(mon_fichier)
    port=d['port']
Addressplayer = ('0.0.0.0', port)
serveraddress=('localhost',3000)
async def listen(): 
    with socket.socket() as s:
        s.settimeout(0.1)
        s.bind(Addressplayer)
        s.listen()
        while True:
            await asyncio.sleep(0)
            try: 
                client, address = s.accept()
                with client:
                    message = client.recv(2048).decode() 
                    requete=json.loads(message)                 
                    if requete["request"]== "ping": 
                        message='{"response": "pong"}'
                        client.send(message.encode())
                    elif requete["request"]=='play':
                        answer=IA2(requete['state'])
                        if answer is  None:
                            answer=IA(requete['state'])
                        message=quelmessagejenvoie(requete['state'])
                        indice={"response": "move",  "move":answer,   "message": message}
                        client.send(json.dumps(indice).encode())
            except socket.timeout:
                pass
