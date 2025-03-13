import requests
import certifi

print(f"certifi path:{certifi.where()}")

#requests.get('https://google.com', verify=certifi.where())

#response = requests.get('https://google.com')
response = requests.get('https://google.com', verify=False)


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
functionName = "TIME_SERIES_INTRADAY"
symbol = "CNI"
apikey = "W54EQ6HJZ4U2JBM0"
url = f'https://www.alphavantage.co/query?function={functionName}&symbol={symbol}&interval=5min&apikey={apikey}'
r = requests.get(url, verify=False) #verify=False, ignoring certificate varification.
data = r.json()

print(data)