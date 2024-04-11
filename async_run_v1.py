import aiohttp
# Allows request to become asynchronous
import asyncio
# Allows event loop and asynchronous in python
import time
import os


# See sync_request.py
# Event Loop : An event loop is when we let some stuff that takes a long time do it's
# thing in the background. And when it's all set, the 'event loop' will 'pick it up'

# Synchronous Function : functionally runs sequentially

# Asynchronous Function : Initiates functions at once and then
# Event loop periodically checks functions that's running. And all the tasks run concurrently.




# Calling API key from Alpha Vantage, example of client side API
# OS is used to get the environment variable
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
# the {} are to get the name in output
# A list of Symbol
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
# A list to store result
results = []


print("Timer started...")
start = time.time()

# We need to make a async function which includes event loop and checks that the processes are done


async def get_symbols():

    # Using aiohttp : using session to get url instead of 'request'
    # session = aiohttp.ClientSession()
    # # Block of Code of API
    # session.close()
    # Instead of session.close(), we can use below way which will automatically
    # close session once job is done
    # In aiohttp/asyncio we use session in place of requests
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            # .format() is used to pass values in {}
            print('Working on symbol {}'.format(symbol))
            # For response to get save somewhere we need to wait, hence await is used.
            # Otherwise, it goes into coroutine, and would return nothing
            response = await session.get(url.format(symbol, api_key), ssl=False)
            results.append(await response.json())
    print('You did it!')


# First we would have to run this function on event loop
# get_symbols()

# Event Loop : Method 1
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_symbols())
# loop.close()

# Or use direct function which does the same thing which above 3 lines does
asyncio.run(get_symbols())
#  USe this code to remove warning from output :loop = asyncio.get_event_loop().run_until_complete(get_symbols())


end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))


