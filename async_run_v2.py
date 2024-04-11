import aiohttp
import asyncio
import time
import os




api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []


print("Timer started...")
start = time.time()


## Using task to fire all the things in event loop at once
## A Synchronous function of task contains list of all the task
def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(session.get(url.format(symbol, api_key), ssl=False))
    # We may use asyncio.create_task(session.get()), which would throw all of them at
    # event loop from here itself, await in responses(line 35) would only wait for them to complete
    # Normally await also throes the responses on loop, if the are not already, but we can do it
    # from here using asyncio.create_task()
    return tasks

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        # Invoking all the tasks at once using gather() of asyncio library
        # *task = it dereferences the list to single uniques parameter values for asyncio
        # otherwise it would be : gather(session.get(TELA API call), session.get(GOOG), session.get(APPL))
        responses = await asyncio.gather(*tasks)
        for response in responses:
            # await is used, since response is an awaitable object
            results.append(await response.json())


# In using asyncio.run(get_symbols()), the 'event loop is closed' warning msg is there in output
# So you may use below for error free
loop = asyncio.get_event_loop().run_until_complete(get_symbols())



end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))


