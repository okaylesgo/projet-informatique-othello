from inscription import inscription
from listen import listen
import asyncio
async def lancement():
    inscription()
    await asyncio.gather(listen())
if __name__=='__main__':
    asyncio.run(lancement())