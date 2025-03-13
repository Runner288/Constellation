import yfinance as yf

def get_stock_info(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)

    # Basic information
    stock_info = stock.info
    print(f"Stock: {stock_info.get('shortName')} ({ticker_symbol})")
    print(f"Current Price: {stock_info.get('regularMarketPrice')}")
    print(f"Market Cap: {stock_info.get('marketCap')}")
    print(f"P/E Ratio: {stock_info.get('trailingPE')}")
    print(f"Dividend Yield: {stock_info.get('dividendYield')}")
    print(f"52-Week High: {stock_info.get('fiftyTwoWeekHigh')}")
    print(f"52-Week Low: {stock_info.get('fiftyTwoWeekLow')}")
    print(f"Previous Close: {stock_info.get('previousClose')}")
    print(f"Open: {stock_info.get('open')}")
    print(f"Volume: {stock_info.get('volume')}")

    # Historical data (last 5 days)
    print("\nHistorical Data (Last 5 Days):")
    hist = stock.history(period="5d")
    print(hist)

if __name__ == "__main__":
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, MSFT): ")
    get_stock_info(ticker)


