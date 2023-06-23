import requests
import time
import json

from typing import List

from flask import Flask

#getSymPrice = 'http://gainers-service:8081/gainers'

app = Flask(__name__)

@app.route('/gainers')
def gainers() -> List[str]:
    # Get the list of top gainers
    url = 'https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=3588dcfb23f5f05c54a69ccc08d83cad'
    response = requests.get(url).json()

    symbols = []
    initialSymbolsAndPrices = []
    updatedSymbolsAndPrices = []
    for gainer in response:
        symbol = gainer['symbol']
        price = gainer['price']
        symbols.append(symbol)
        symbols.append(price)
        initialSymbolsAndPrices.append(symbol)
        initialSymbolsAndPrices.append(price)
        if len(symbols) == 10:
            break

    # Wait for 5 seconds
    time.sleep(5)

    # Get the updated prices of the same symbols
    for i in range(0, len(symbols), 2):
        symbol = symbols[i]
        symbolUrl = 'https://financialmodelingprep.com/api/v3/quote/' + symbol + '?apikey=3588dcfb23f5f05c54a69ccc08d83cad'
        symbolResponse = requests.get(symbolUrl).json()
        price = symbolResponse[0]['price']
        symbols[i + 1] = price
        updatedSymbolsAndPrices.append(symbol)
        updatedSymbolsAndPrices.append(price)

    # Combine the initial symbols and prices with the updated symbols and prices
    result = []
    result.append('Initial symbols and prices:')
    result.extend(initialSymbolsAndPrices)
    result.append('')
    result.append('Symbols and prices after 30mins:')
    result.extend(updatedSymbolsAndPrices)

    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
