#testing
import yfinance as yf
import pandas as pd 
import datetime as dt

from datetime import datetime, timedelta

# new goal as of 12/28: need to get a lot more fucking data (many stocks, many options..)

nasdaq_100_tickers = [
    "AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "NVDA", "META", "PEP", "NFLX", "ADBE",
    "AVGO", "INTC", "CMCSA", "CSCO", "COST", "TMUS", "TXN", "QCOM", "AMGN", "HON",
    "AMD", "INTU", "SBUX", "AMAT", "GILD", "BKNG", "ADP", "MDLZ", "ISRG", "REGN",
    "PDD", "PYPL", "MU", "MRNA", "FISV", "KLAC", "MAR", "VRTX", "LRCX", "CTSH",
    "CSX", "ADI", "SNPS", #"ATVI", 
    "NXPI", "ORLY", "EA", "IDXX", "PANW", "MNST",
    "KDP", "FTNT", "AZN", "ROST", "CHTR", "TEAM", "CDNS", "EXC", "AEP", 
    #"SGEN",
    "WDAY", "MELI", "DXCM", "XEL", "CRWD", "PCAR", "LCID", "ALGN", "ENPH", "VRSK",
    "ZS", "DDOG", "OKTA", "BIDU", "DOCU", "BIIB", "ANSS", "MRVL", "PAYC", "ZS", 
    "JD", "CTAS", "PINS", "EBAY", "TTWO", #"SPLK", 
    "CPRT", #"SGEN", 
    "ODFL", "BKR", "NTES", "CEG", "FAST", "MTCH"
]

exp_date = '2025-01-17'
options_data = []

# right now model trains only works for one stock, one date.
# ideally, woudl be able to scale such that multipke stocks, multiple dates can be looked at
# ideally, even more data that points to some option price at x expiry date


for ticker in nasdaq_100_tickers:

    try:
        ticker = yf.Ticker(ticker)
        options = ticker.option_chain(date=exp_date)

        calls = options.calls
        puts = options.puts

        today = dt.datetime.now()
        time_to_maturity = (dt.datetime.strptime(exp_date, "%Y-%m-%d") - today).days / 365
        
        calls["time_to_maturity"] = time_to_maturity
        puts["time_to_maturity"] = time_to_maturity

        calls["option_type"] = 1
        puts["option_type"] = 0

        columns = ['strike', 'lastPrice', 'impliedVolatility', 'openInterest', 'volume', 
                'time_to_maturity', 'option_type']
        calls = calls[columns]
        puts = puts[columns]

        stock_options = pd.concat([calls, puts], ignore_index=True)

        # stock_options['ticker'] = ticker

        hist_data = ticker.history(period='1y')
        hist_data['daily_return'] = hist_data['Close'].pct_change()
        hist_data['volatility_30d'] = hist_data['daily_return'].rolling(window=30).std() * (252 ** 0.5)

        recent_volatility = hist_data['volatility_30d'].iloc[-1]
        stock_options['historical_volatility'] = recent_volatility

        current_data = ticker.history(period="1d")
        current_stock_price = current_data['Close'].iloc[-1]

        stock_options["strike_ratio"] = stock_options["strike"] / current_stock_price
        stock_options["lastPrice_ratio"] = stock_options["lastPrice"] / current_stock_price
        stock_options["openInterest_ratio"] = stock_options["openInterest"] / (stock_options["volume"] + 1e-9)

        options_data.append(stock_options)

    except Exception as e:
        print(f"Failed for {ticker}: {e}")


nasdaq_100_data = pd.concat(options_data, ignore_index=True)
nasdaq_100_data.to_csv("~/Downloads/nasdaq_100_options_test10.csv", index=False)










    
