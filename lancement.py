#C'est avec cette fonction que nous lançons le programme. 
# Nous pouvons mettre le port que nous voulons utiliser 
# ainsi que le pseudo et le matricule que nous voulons. 
#Vous pouvez aussi lancer le programme sans rien y ajouter. Un port,un pseudo et un matricule
#vous seront donnés.

from inscription import inscription
from listen import listen
import asyncio
async def lancement():
    inscription()
    await asyncio.gather(listen())
if __name__=='__main__':
    asyncio.run(lancement())