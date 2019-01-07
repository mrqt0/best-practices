# write one coroutine for asnychronous logging

import asyncio
import concurrent.futures
import functools
import threading
import time

f = open("trace.log", "w")

async def tracer(loop):
    # with open("trace.log", "w") as f:
    for i in range(10):
        await asyncio.sleep(1)
        f.write("{}\n".format(loop.time()))
            # print(loop.time())

def add_comment(comment):
# with open("trace.log", "w") as f:
    f.write(comment)

# get event loop from other thread or pass to thread?

def thread_main(new_loop):
    new_loop.run_until_complete(tracer(new_loop))
    new_loop.close()

def iface(new_loop):
    inp = None
    while inp != "q":
        inp = input()
        new_loop.call_soon_threadsafe(functools.partial(add_comment, inp))

def main():

    new_loop = asyncio.new_event_loop()
    thread = threading.Thread(target=thread_main, args=(new_loop,))
    t2 = threading.Thread(target=iface, args=(new_loop,))

    thread.start()
    t2.start()
    thread.join()
    t2.join()

    f.close()


main()