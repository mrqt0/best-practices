import asyncio
import functools
import signal 

async def coro(loop):
    # for signame in {'SIGINT', 'SIGTERM'}:
    #     loop.add_signal_handler(
    #         getattr(signal, signame),
    #         loop.stop())
    try:
        await asyncio.sleep(10)
    except KeyboardInterrupt:
        loop.stop()

async def wakeup():
    while True:
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            loop.stop()

def foo():
    loop = asyncio.get_event_loop()
    # asyncio.ensure_future(wakeup())
    # try:
    loop.run_until_complete(coro(loop))
    # except KeyboardInterrupt:
        # pass
    loop.close()

foo()
# loop.run_until_complete()
