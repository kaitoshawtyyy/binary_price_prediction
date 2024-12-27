import pandas as pd
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import Input
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from data_processing import processed_df, scaler_y


X = processed_df.drop('lastPrice', axis=1)
y = processed_df['lastPrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()

model.add(Input(shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

predictions = model.predict(X_test)

# Ensure predictions are reshaped as 2D
predictions = predictions.reshape(-1, 1)

# Apply inverse transformation to predictions
predictions_actual = scaler_y.inverse_transform(predictions)



print(predictions)
print(predictions_actual)