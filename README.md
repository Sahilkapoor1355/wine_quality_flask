# 🍷 Wine Prediction Web App

A web application built with **Flask**, **NumPy**, and **Joblib** that takes 11 physicochemical wine features from a web form and returns predictions from a pre-trained machine learning model (`wine_model.joblib`).

---

## ✨ Features

- **Real-Time ML Inference:** Loads `wine_model.joblib` and runs predictions on user-submitted values via `model.predict`.
- **Interactive Web Form:** Collects all 11 input features through an HTML template (`templates/index.html`) and renders the prediction back on the page.
- **Lightweight Flask Backend:** Handles both `GET` and `POST` requests on `/` cleanly in Python.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Machine Learning & Data:** NumPy, Joblib (`wine_model.joblib`)
- **Frontend:** HTML (`templates/index.html`) rendered with Jinja2 via `render_template`

---

## 📂 Project Structure

```text
├── app.py                 # Flask application and prediction route
├── wine_model.joblib      # Serialized pre-trained ML model
└── templates/
    └── index.html         # Web form and prediction display template
