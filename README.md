# House Price Prediction App (Amsterdam Housing Dataset)
This is a Flask-based web application that predicts house prices in Amsterdam using a machine learning model trained with the Random Forest Regressor. Users can input various property features, and the app will output the estimated price.


## ⚙️ How It Works

1. `model.py`:
   - Loads and cleans the dataset.
   - Removes outliers and irrelevant columns.
   - Trains a `RandomForestRegressor`.
   - Saves the trained model and feature names.

2. `app.py`:
   - Loads the saved model and feature list.
   - Provides a web form for users to input property features.
   - Predicts and displays the estimated house price.

---

## 🧪 Requirements

Install dependencies with:

bash or Terminal
pip install flask pandas scikit-learn joblib


## 🚀 Getting Started
### Clone the repository

git clone <https://github.com/pratikraogithub/House_Price_Predictor>
Then in terminal or bash type - cd house_price_app

```python
print("Code block")
```