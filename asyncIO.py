import asyncio
import time

# Asyncio : Method used to concurrently execute code
# In general python runs code sequentially

def first_function():
    time.sleep(3)
    print("funct1")

def second_function():
    time.sleep(3)
    print("funct2")


def third_function():
    time.sleep(3)
    print("funct3")


# Async Functions
async def fourth_function():
    print("funct4")
    await asyncio.sleep(2)



# We use await asyncio.sleep() : this would make
async def fifth_function():
    print("funct5")
    await asyncio.sleep(2)



async def sixth_function():
    print("funct6")
    await asyncio.sleep(2)


async def main():
    # Await : it just waits for that function to be finished
    # We create task like below which would make function 4th run at any time when we get time, this task is scheduled.
    # But this way is not a organised manner, hence we use gather
    # task = await asyncio.create_task(sixth_function())
    # await fourth_function()
    # await fifth_function()
    L = await asyncio.gather(
       fourth_function(),
       fifth_function(),
        sixth_function()
        )
    print(L)


first_function()
second_function()
third_function()
asyncio.run(main())

















