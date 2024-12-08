import asyncio

async def my_coroutine():
    print(f"Start {__name__}")
    await asyncio.sleep(3)
    print(f"End {__name__}")
    return 'result'
    


async def my_async_function():
    print(f"Starting async function {__name__}")
    await asyncio.sleep(5)  # Pause execution for 10 seconds
    print(f"ending async function {__name__}")
    return 'result2'

async def main():
    print(f"Starting main function {__name__}")
    # task = asyncio.create_task(my_async_function())  # Wait for async function to complete
    task = asyncio.gather(my_coroutine(), my_async_function())
    a, b = await task
    print(f"Ending main function {__name__}")
    # await task
    return dict(a=a, b=b)

result = asyncio.run(main())
print(result)