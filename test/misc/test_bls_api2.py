import requests
import json

# Replace this with your BLS API key
API_KEY = 'e80a19771e034aa4872c6101a44ae98b'

# Define the endpoint URL for the BLS API
url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

# Specify the parameters for the request
# Example: Retrieve unemployment rate for a specific time series (e.g., "LNS14000000" for national unemployment rate)
params = {
    'registrationKey': API_KEY,
    'startyear': '2020',
    'endyear': '2023',
    'seasonality': 'S',
    'seriesid': ['LNS14000000'],  # List of series IDs you want to query
}

# Send the GET request to the BLS API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Check if the response contains data
    if data['status'] == 'REQUEST_SUCCEEDED':
        # Print the time series data
        for series in data['Results']['series']:
            print(f"Series ID: {series['seriesID']}")
            for data_point in series['data']:
                print(f"Year: {data_point['year']}, Month: {data_point['periodName']}, Value: {data_point['value']}")
    else:
        print("Error: No data returned or invalid series ID.")
else:
    print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
