#testing
import yfinance as yf
import pandas as pd 
import datetime as dt

# relevant info
# strike price, stock price, time to maturity, implied volatility,
# risk free rate, option type, open interest, historical volatility, volume 
# 
# dependent var we try to predict -> option price 

# historical volatility requires calc, so does open interest (which is call specific)

ticker = yf.Ticker('AAPL')
exp_date = '2025-01-03'
options = ticker.option_chain(date = exp_date)
calls = options.calls
puts = options.puts 

#time stuff

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

df = pd.concat([calls, puts], ignore_index=True)

# historical volatility stuff

hist_data = ticker.history(period='1y')
hist_data['daily_return'] = hist_data['Close'].pct_change()
hist_data['volatility_30d'] = hist_data['daily_return'].rolling(window=30).std() * (252 ** 0.5)

recent_volatility = hist_data['volatility_30d'].iloc[-1]
df['historical_volatility'] = recent_volatility

df.to_csv("~/Downloads/opt_test2.csv", index=False)


# right now this only works for oen stock, one date.
# ideally, woudl be able to scale such that multipke stocks, multiple dates can be looked at
# ideally, even more data that points to some option price at x expiry date



