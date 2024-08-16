import asyncio


async def func1():
    for i in range(3):
        print("Func1")
        await asyncio.sleep(1)


async def func2():
    for i in range(4):
        print("Func2")
        await asyncio.sleep(0.5)


async def main():

    await asyncio.gather(
        func1(),
        func2()
    )


asyncio.run(main())

print("End of program")
