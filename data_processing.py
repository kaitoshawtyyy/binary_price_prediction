# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler
# from data_acquisition import nasdaq_100_data

# # drop rows with missing data -> idk why this is occurring yet 
# df = nasdaq_100_data.dropna(subset=['lastPrice', 'impliedVolatility', 'time_to_maturity', 'openInterest', 
#                        'volume', 'option_type', 'historical_volatility', 'strike_ratio', 
#                        'lastPrice_ratio', 'openInterest_ratio' ])

# df_unscaled = df.copy()

# # these features are gonna be bound between 0-1, that way models work better 
# features_scaled = ['strike_ratio', 'impliedVolatility', 'lastPrice_ratio', 'openInterest_ratio', 'volume', 'historical_volatility']

# # converted features_scaled to floating pt values
# df[features_scaled] = df[features_scaled].apply(pd.to_numeric, errors='coerce')
# df[features_scaled] = df[features_scaled].astype('float64')

# # using minmaxscaler
# scaler_X = MinMaxScaler()

# #modify the existing dataframe to scale
# df[features_scaled] = df[features_scaled].astype(float)
# df.loc[:, features_scaled] = scaler_X.fit_transform(df[features_scaled])


# scaler_y = MinMaxScaler()
# df['lastPrice_ratio'] = scaler_y.fit_transform(df[['lastPrice_ratio']].astype(float))

# processed_df = df

# print(processed_df)




