import yfinance as yf

# Fetch ticker
ticker = yf.Ticker('AAPL')

print("Available Expirations:", ticker.options)