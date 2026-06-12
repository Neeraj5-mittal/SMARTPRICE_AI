# 🏠 SmartPrice AI — Real Estate Price Prediction System

## 🚀 Overview
SmartPrice AI is a Machine Learning-powered web application that predicts real estate prices based on property features like location, area (sqft), number of bedrooms, bathrooms, and more.

It combines:
- Machine Learning Model (Scikit-learn)
- FastAPI Backend (API service)
- Streamlit Frontend (User interface)
- Data preprocessing & feature engineering pipeline

---

## 🎯 Features
- 🔮 Predict house prices instantly
- 📍 Location-based price estimation
- 🧠 Trained ML regression model
- ⚡ FastAPI backend for prediction API
- 🎨 Streamlit UI for easy interaction
- 📊 Cleaned and processed dataset pipeline

---

## 🏗️ Architecture
```text
User Interface (Streamlit)
        ↓
FastAPI Backend (main.py)
        ↓
ML Model (house_price_model.pkl)
        ↓
Prediction Output

SmartPrice-AI/
│
├── backend/
│   ├── main.py
│   ├── model_loader.py
│   ├── schemas.py
│
├── frontend/
│   └── app.py
│
├── src/
│   ├── data_cleaning.py
│   ├── outlier_removal.py
│   ├── sqft_cleaning.py
│   ├── train_model.py
│   ├── predict.py
│   └── test_data.py
│
├── models/
│   ├── house_price_model.pkl
│   └── model_columns.pkl
│
├── datasets/
│   └── house/
│       ├── bengaluru_house_prices.csv
│       ├── cleaned_house_data.csv
│       └── processed_house_data.csv
│
├── requirements.txt
└── README.md

```

## 🚀 Run Project

### ▶ Backend (FastAPI)
```bash
uvicorn backend.main:app --reload
```
API will run at:

http://127.0.0.1:8000
🎨 Frontend (Streamlit)
streamlit run frontend/app.py

## 📊 Sample Prediction

## Input:
- Location: Bangalore  
- Area: 1200 sqft  
- Bedrooms: 2  
- Bathrooms: 2  

## Output:
```text
Estimated Price: ₹ 65,00,000
```
##🧠 Machine Learning Workflow
- Data Cleaning
- Feature Engineering
- Outlier Removal
- Model Training
- Model Evaluation
- Model Saving (.pkl)
- Deployment using FastAPI

## 🛠 Tech Stack
- Python 🐍
- Pandas & NumPy 📊
- Scikit-learn 🤖
- FastAPI ⚡
- Streamlit 🎨

## 🚀 Future Improvements
- Deploy on AWS / Render / Streamlit Cloud
- Improve model accuracy (XGBoost / Random Forest)
- Add authentication system
- Add real-time data integration
- Improve UI/UX design


##👨‍💻 Author
Neeraj Mittal
Data Science & AI/ML Enthusiast 🚀

⭐ Support

If you like this project, please give it a ⭐ on GitHub!
