import yfinance as yf
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl

# Custom adapter to ignore SSL verification
class UnsafeAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        kwargs['ssl_context'] = context
        return super(UnsafeAdapter, self).init_poolmanager(*args, **kwargs)

# Override requests' default session
session = requests.Session()
session.mount('https://', UnsafeAdapter())

# Pass the session to yfinance
def get_stock_info(ticker_symbol):
    stock = yf.Ticker(ticker_symbol, session=session)
    stock_info = stock.info
    print(f"Stock: {stock_info.get('shortName')} ({ticker_symbol})")
    print(f"Current Price: {stock_info.get('regularMarketPrice')}")
    print(f"Market Cap: {stock_info.get('marketCap')}")

if __name__ == "__main__":
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, MSFT): ")
    get_stock_info(ticker)
