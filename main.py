import asyncio
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

def func():
    queue = multiprocessing.Queue()

async def submit():
    loop = asyncio.get_running_loop()
    num = 2
    executor = ThreadPoolExecutor(max_workers=num)

    futs = []
    for i in range(num):
        futs.append(loop.run_in_executor(executor, func))

    for fut in futs:
        await fut

if __name__ == '__main__':
    asyncio.run(submit())
