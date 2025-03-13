
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.optimizers import Adam
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Function to fetch stock data
def get_stock_data(ticker, period="5y"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df

# Function to estimate fair value using a simple DCF model
def discounted_cash_flow(earnings, growth_rate=0.05, discount_rate=0.08, years=5, terminal_value=30):
    cash_flows = [(earnings * (1 + growth_rate) ** i) / (1 + discount_rate) ** i for i in range(1, years + 1)]
    terminal_value_discounted = terminal_value / (1 + discount_rate) ** years
    return sum(cash_flows) + terminal_value_discounted

# Function to calculate stock risk (Beta)
def calculate_beta(stock_ticker, market_ticker="^GSPC", period="5y"):
    stock_data = get_stock_data(stock_ticker, period)["Close"].pct_change().dropna()
    market_data = get_stock_data(market_ticker, period)["Close"].pct_change().dropna()
    
    combined_data = pd.concat([stock_data, market_data], axis=1, keys=[stock_ticker, market_ticker]).dropna()
    X = combined_data[market_ticker].values.reshape(-1, 1)
    y = combined_data[stock_ticker].values.reshape(-1, 1)
    
    model = LinearRegression()
    model.fit(X, y)
    beta = model.coef_[0][0]
    return beta

# Function to compare stock with industry peers
def industry_comparison(ticker):
    stock = yf.Ticker(ticker)
    pe_ratio = stock.info.get("trailingPE", None)
    pb_ratio = stock.info.get("priceToBook", None)
    
    print(f"{ticker} Valuation Metrics:")
    print(f"P/E Ratio: {pe_ratio}")
    print(f"P/B Ratio: {pb_ratio}")

# Function to predict stock prices using LSTM
def predict_stock_prices_lstm(ticker, days_ahead=30):
    df = get_stock_data(ticker, period="5y")
    df["Close"] = df["Close"].fillna(method="ffill")
    
    # Prepare data for LSTM
    data = df["Close"].values.reshape(-1, 1)
    scaler = tf.keras.preprocessing.MinMaxScaler()
    data = scaler.fit_transform(data)
    
    X, y = [], []
    sequence_length = 60
    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    
    X, y = np.array(X), np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build LSTM model
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(sequence_length, 1)),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(25, activation="relu"),
        Dense(1)
    ])
    
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
    model.fit(X_train, y_train, batch_size=16, epochs=20, validation_data=(X_test, y_test))
    
    # Predict future prices
    future_data = data[-sequence_length:].reshape(1, sequence_length, 1)
    future_prices = []
    for _ in range(days_ahead):
        pred = model.predict(future_data)[0, 0]
        future_prices.append(pred)
        future_data = np.roll(future_data, -1, axis=1)
        future_data[0, -1, 0] = pred
    
    future_prices = scaler.inverse_transform(np.array(future_prices).reshape(-1, 1))
    
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"], label="Actual Prices")
    plt.plot(pd.date_range(df.index[-1], periods=days_ahead, freq='D'), future_prices, linestyle='dashed', label="Predicted Prices (LSTM)")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.show()

# Function to fetch news sentiment analysis
def get_news_sentiment(ticker):
    url = f"https://www.google.com/search?q={ticker}+stock+news"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = [h.text for h in soup.find_all("h3")][:5]
    
    sentiment_scores = [TextBlob(headline).sentiment.polarity for headline in headlines]
    average_sentiment = np.mean(sentiment_scores)
    
    print(f"News Sentiment Score for {ticker}: {average_sentiment:.2f} (Positive if > 0, Negative if < 0)")
    print("Recent Headlines:")
    for headline in headlines:
        print(f"- {headline}")

# Main function to analyze a stock
def analyze_stock(ticker):
    print(f"Analyzing {ticker}...")
    stock = yf.Ticker(ticker)
    earnings = stock.financials.loc["Net Income"].iloc[0] / stock.info["sharesOutstanding"]
    fair_value = discounted_cash_flow(earnings)
    beta = calculate_beta(ticker)
    
    print(f"Estimated Fair Value (DCF): ${fair_value:.2f}")
    print(f"Stock Beta (Risk Level): {beta:.2f}")
    industry_comparison(ticker)
    
    print("Predicting future prices using LSTM...")
    predict_stock_prices_lstm(ticker)
    
    print("Fetching news sentiment analysis...")
    get_news_sentiment(ticker)

# Example usage
ticker_symbol = "AAPL"  # Change to any stock symbol
analyze_stock(ticker_symbol)
