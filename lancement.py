from inscription import inscription
from listen import listen
import asyncio
async def lancement():
    inscription()
    await asyncio.gather(listen())
asyncio.run(lancement())