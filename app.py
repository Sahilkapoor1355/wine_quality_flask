
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('wine_model.joblib')

cols = [
    'fixed acidity',
    'volatile acidity',
    'citric acid',
    'residual sugar',
    'chlorides',
    'free sulfur dioxide',
    'total sulfur dioxide',
    'density',
    'pH',
    'sulphates',
    'alcohol'
]


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        In = []

        for col in cols:
            value = float(request.form[col])
            In.append(value)

        out = model.predict([In])
        prediction = out[0]

    return render_template('index.html',
                           cols=cols,
                           prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
