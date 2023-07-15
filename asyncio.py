import asyncio

async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")

# asyncio.run(my_coroutine())



async def my_async_function():
    print("Starting async function")
    await asyncio.sleep(10)  # Pause execution for 10 seconds
    print("Resuming async function")

async def main():
    print("Starting main function")
    task = asyncio.create_task(my_async_function())  # Wait for async function to complete
    print("Ending main function")
    await task

asyncio.run(main())


import abc





