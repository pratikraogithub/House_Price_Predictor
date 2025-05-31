# app.py (Updated)
from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load model and features
model = joblib.load('rf_model.pkl')
features = joblib.load('features.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            input_data = [float(request.form[feature]) for feature in features]
            input_array = np.array(input_data).reshape(1, -1)
            prediction = model.predict(input_array)[0]
            return render_template('index.html', prediction=round(prediction, 2), features=features)
        except:
            return render_template('index.html', prediction="Invalid input. Please enter numeric values.", features=features)
    
    return render_template('index.html', prediction=None, features=features)

if __name__ == '__main__':
    app.run(debug=True)
