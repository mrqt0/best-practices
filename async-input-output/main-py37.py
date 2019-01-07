import asyncio

# awaitable: something that can be used in await statement
# - coroutine:
# - task: schedule execution of coroutine immediately
# - future: special object, coroutine will wait until future is 'resolved'


async def main():
    """Python 3.7 style without event loop.

    Several high level functions were introduced so
    there is not need to access the event loop.

    """

    # run one after another
    print("Await")
    await coro1()
    await coro2()

    # create task and schedule to run soon concurrently
    # new in python 3.7
    print("Create tasks")
    t1 = asyncio.create_task(coro1())
    t1.add_done_callback(lambda future: print("Done"))
    t2 = asyncio.create_task(coro2())
    # wait for completion of first task, cancel second
    await t1
    # cancel task, i.e. send CancelledError to coroutine
    t2.cancel()

    # schedule and wait concurrently
    # returns results of tasks in insertion order
    # stops on first excpetion, unless return_exceptions = True
    print("Gather")
    await asyncio.gather(coro1(), coro2())

    # or wait on multiple
    # returns two sets of tasks: done and pending
    # tasks are not cancelled after timeout, will be returned as pending
    # passing coroutine objects discouraged, because task will be returned
    print("Wait")
    tasks = [asyncio.create_task(coro1()), asyncio.create_task(coro2())]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("Done:", done)
    print("Pending:", pending)
    print("Current task:", asyncio.current_task())
    print("Pending tasks:", asyncio.all_tasks())

    for task in pending:
        task.cancel()

    # run, but with timeout for cancellation
    # will raise timeout error
    print("Wait for")
    try:
        await asyncio.wait_for(coro1(), 0.2)
    except asyncio.TimeoutError:
        # TODO: this seems not to be the exception, how to catch it?
        pass

    print("As completed")
    # iterate in order in whihc they are finished
    for future in asyncio.as_completed([coro1(), coro2()]):
        await future
        print("Done")


    await low_level()


async def error_handling_example():
    pass
    # await: can handle excpetions with try: .. except: ..
    # create_task (ensure_future): exceptions might go unnoticed
    # only when retrieving result
    # in callback (e.g. done callback): mutate list of 
    # or in gather set

async def low_level():
    # if you still need to access event loop
    loop = asyncio.get_running_loop()
    



async def coro1():
    for i in range(3):
        print("hello1", i)
        await asyncio.sleep(0.1)

async def coro2():
    for i in range(5):
        print("hello2", i)
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            print("Coro2 cancelled")


if __name__ == "__main__":
    asyncio.run(main())

