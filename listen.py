import socket
import asyncio
import json
import sys
port=int(sys.argv[1])
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
                        None
                        #IA A FAIRE
            except socket.timeout:
                pass