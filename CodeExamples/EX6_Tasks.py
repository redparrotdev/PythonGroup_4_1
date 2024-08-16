import asyncio



async def some_process():
    await asyncio.sleep(5)
    print("End of sleep")


async def main():
    task = asyncio.create_task(some_process())

    for i in range(20):
        await asyncio.sleep(0.5)
        print(i)

    await task



asyncio.run(main())
