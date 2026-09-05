# ====================== what is async and await ======================
# async is a keyword in Python that is used to define an asynchronous function.
# await is a keyword in Python that is used to define an asynchronous function.
# asyncio is a module in Python that is used to define an asynchronous function.

import asyncio

# Async def main
async def main(name):
    print(f"Hello World {name}")

asyncio.run(main("Faruk"))


# Async def main with await asyncio.sleep(1)
async def main(name):
    print(f"Hello World {name}")
    await asyncio.sleep(1)
    print(f"Hello World {name}")

asyncio.run(main("Faruk"))


