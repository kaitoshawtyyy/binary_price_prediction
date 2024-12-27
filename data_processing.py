import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from data_acquisition import df


# drop rows with missing data -> idk why this is occurring yet 
df = df.dropna(subset=['lastPrice', 'impliedVolatility', 'time_to_maturity', 'openInterest', 'volume', 'option_type', 'historical_volatility'])

#t hese features are gonna be bound between 0-1, that way models work better 
features_scaled = ['strike', 'impliedVolatility', 'openInterest', 'volume', 'historical_volatility']

# using minmaxscaler
scaler_X = MinMaxScaler()

#modify the existing dataframe to scale
df[features_scaled] = df[features_scaled].astype(float)
df.loc[:, features_scaled] = scaler_X.fit_transform(df[features_scaled])


scaler_y = MinMaxScaler()
df['lastPrice'] = scaler_y.fit_transform(df[['lastPrice']])

processed_df = df

print(processed_df)

# so this should work, for some reason notebook doesn't reflect same changes.
# this does predict a price.. verify that its actually kinda sensible tmrw.. 12/26

