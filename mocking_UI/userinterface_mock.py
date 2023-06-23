import requests
from datetime import datetime, timedelta
import pytz

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
total_percent_change = 0
total_count = 0
investment_amount = float(input("How much money would you like to put in? "))
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
        total_percent_change += percent_change
        total_count += 1
    else:
        price_at_10am = 'N/A'
        percent_change = 'N/A'

    # Calculate the win or loss based on the investment amount and percent change for the current ticker
    win_or_loss = investment_amount * (percent_change / 100)

    # Create a dictionary with the ticker, percent gain, and win or loss and append it to the list
    symbol_and_price = {
        'ticker': symbol,
        'percent_gain': f'{percent_change:.2f}%',
        'win_or_loss': f'${win_or_loss:.2f}'
    }
    symbols_and_prices.append(symbol_and_price)

# Calculate the average percent change
average_percent_change = total_percent_change / total_count if total_count > 0 else 0

# Calculate the total win or loss based on the investment amount and the average percent change
total_win_or_loss = investment_amount * (average_percent_change / 100)

# Print the top 5 gainers with their percent gains and win or losses
for symbol_and_price in symbols_and_prices:
    print(symbol_and_price)

# Print the investment amount, average percent gain, and total win or loss
print(f"Investment amount: ${investment_amount}")
print(f"Average percent gain: {average_percent_change:.2f}%")
print(f"Total win or loss: ${total_win_or_loss:.2f}")
