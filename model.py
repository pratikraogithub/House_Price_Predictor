# model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load and clean data
df = pd.read_csv('Amsterdam.csv')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.drop(columns=['Address', 'Zip', 'Unnamed: 0'], axis=1, inplace=True)

# Outlier removal
numerical_columns = df.select_dtypes(exclude=object).columns.tolist()
for col in numerical_columns:
    upper_limit = df[col].mean() + 3 * df[col].std()
    lower_limit = df[col].mean() - 3 * df[col].std()
    df = df[(df[col] <= upper_limit) & (df[col] >= lower_limit)]

X = df.drop(['Price'], axis=1)
y = df['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)

# Save model and feature columns
joblib.dump(rf, 'rf_model.pkl')
joblib.dump(X.columns.tolist(), 'features.pkl')
