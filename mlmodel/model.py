# Import necessary libraries
import sys
sys.path.insert(0, r"/opt/homebrew/lib/python3.9/site-packages/pandas")
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Load your dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
dataset = pd.read_csv('dataset/crime.csv', encoding= 'unicode_escape')

# Select relevant columns
features = ['offense_type_id', 'offense_category_id', 'reported_date', 'geo_lon', 'geo_lat']
target = 'is_crime'  # Assuming you have a binary label indicating whether a crime occurred or not

# Convert reported_date to datetime and extract relevant features
dataset['reported_date'] = pd.to_datetime(dataset['reported_date'])
dataset['day_of_week'] = dataset['reported_date'].dt.dayofweek
dataset['hour_of_day'] = dataset['reported_date'].dt.hour
dataset['month'] = dataset['reported_date'].dt.month

# Create a binary column indicating whether a crime occurred
dataset['is_crime'] = 1  # You'll need to replace this with your actual label data

# Drop unnecessary columns
dataset = dataset[['offense_type_id', 'offense_category_id', 'day_of_week', 'hour_of_day', 'month', 'geo_lon', 'geo_lat', 'is_crime']]

# Split the dataset into features and labels
X = dataset.drop('is_crime', axis=1)
y = dataset['is_crime']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build a simple neural network model
model = Sequential()
model.add(Dense(64, input_dim=X_train_scaled.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f'Test Accuracy: {accuracy * 100:.2f}%')
