import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and the time period
stock_symbol = 'AAPL'
start_date = '2025-01-01'
end_date = '2025-01-25'

# Fetch the historical data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the data
print(stock_data.head())

# Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(stock_data['Close'], label='Close Price')
plt.title(f'Closing Prices of {stock_symbol}')
plt.xlabel('Date')
plt.ylabel('Close Price USD')
plt.legend()
plt.grid()
plt.show()
