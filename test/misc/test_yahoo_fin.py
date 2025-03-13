from yahoo_fin import stock_info as si

# Function to get stock data
def get_stock_data(ticker):
    try:
        # Get current price
        price = si.get_live_price(ticker)
        
        # Get financial summary
        quote_table = si.get_quote_table(ticker)

        # Get historical data (last 5 days)
        historical_data = si.get_data(ticker, start_date=None, end_date=None, index_as_date=True, interval="1d")
        last_5_days = historical_data.tail(5)

        # Print data
        print(f"Live price of {ticker}: ${price:.2f}\n")
        print("Financial Summary:")
        for key, value in quote_table.items():
            print(f"{key}: {value}")
        
        print("\nHistorical Data (Last 5 Days):")
        print(last_5_days)
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example: Get data for Apple (AAPL)
get_stock_data("AAPL")
