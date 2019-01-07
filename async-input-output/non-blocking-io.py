"""
Use locks for printing to stdout
When locked: print to buffer? Wait? Do nothing?
"""

import asyncio

FILENAME = "log.log"

async def iface():
    loop = asyncio.get_running_loop()
    inp = await loop.run_in_executor(None, input)
    with open(FILENAME, "a") as f:
        f.write(inp + "\n")

async def log():
    loop = asyncio.get_running_loop()
    for i in range(10):
        with open(FILENAME, "a") as f:
            f.write(f"{i}: {loop.time()}\n")
        await asyncio.sleep(1)    
    
async def main():
    await asyncio.gather(iface(), log())

if __name__ == "__main__":
    asyncio.run(main())
