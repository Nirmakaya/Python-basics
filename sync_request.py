import time
import requests
# To make the API call
import os
# to have some environment variable

# Calling free API key from Alpha Vantage
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
# the {} are to get the name in output
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []


print("Timer started...")
start = time.time()

for symbol in symbols:
    print('Working on symbol {}'.format(symbol))
    # response module is used to request data from a server.
    # The data is typically in the form of a file or a web page
    response = requests.get(url.format(symbol, api_key), verify=False)
    results.append(response.json())
print('You did it!')



end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))

