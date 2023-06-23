import requests
import pytz
from datetime import datetime
from .producer import publish
def post_data_to_api(data):
    url = "http://localhost:8000/api/products"
    response = requests.post(url, json=data)
    return response
def fetch_stock_data_and_publish():
    # Get the current time in New York
    ny_time = datetime.now(pytz.timezone('US/Eastern'))

    # Format the time as a string for the API call
    ny_time_str = ny_time.strftime('%Y-%m-%d %H:%M:%S')

    # Define the function to calculate percent change based on start and current price
    def calculate_percent_change(start_price, current_price):
        return (current_price - start_price) / start_price * 100

    url = f'https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=2f212cd3f9049264fe6232846363a477'
    response = requests.get(url).json()

    symbols_and_prices = []
    for gainer in response[:5]:
        symbol = gainer['symbol']
        price = gainer['price']

        # Get the historical price at 10 am
        historical_url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey=2f212cd3f9049264fe6232846363a477&from={ny_time_str}&to={ny_time_str}'
        historical_response = requests.get(historical_url).json()

        # Check if there is data for 10 am
        if len(historical_response['historical']) > 0:
            price_at_10am = historical_response['historical'][0]['open']
            percent_change = calculate_percent_change(price_at_10am, price)
        else:
            price_at_10am = 'N/A'
            percent_change = 'N/A'

        # Create a dictionary with the symbol and percent change and append it to the list
        symbol_and_price = {
            'title': symbol,
            'image': f'{percent_change}%'
        }
        symbols_and_prices.append(symbol_and_price)

    # Print the top 5 gainers with their percent changes
    for symbol_and_price in symbols_and_prices:
        post_data_to_api(symbol_and_price)
        for symbol_and_price in symbols_and_prices:
            response = post_data_to_api(symbol_and_price)
            if response.status_code == 201:
                print("Data posted successfully")
            else:
                print(f"Failed to post data with status code: {response.status_code}")

