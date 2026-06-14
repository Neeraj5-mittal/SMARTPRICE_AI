# 🏠 SmartPrice AI — Real Estate Price Prediction System

## 🚀 Overview

SmartPrice AI is an end-to-end Machine Learning web application that predicts residential property prices based on key features such as location, square footage, number of bedrooms, and bathrooms.

The project demonstrates the complete ML lifecycle, including data preprocessing, feature engineering, model training, API development, and deployment.

### 🔗 Live Demo

https://smartprice-ai-9.onrender.com

---

## ✨ Key Features

* 🔮 Real-time property price prediction
* 📍 Location-based valuation
* 🧠 Machine Learning regression model
* ⚡ FastAPI-powered REST API
* 🎨 Interactive Streamlit user interface
* 📊 Data cleaning and feature engineering pipeline
* 🚀 Cloud deployment on Render

---

## 🏗️ System Architecture

```text
Streamlit Frontend
       │
       ▼
FastAPI Backend
       │
       ▼
Trained ML Model (.pkl)
       │
       ▼
Predicted Property Price
```

---

## 📂 Project Structure

```text
SmartPrice-AI/
│
├── backend/
│   ├── main.py
│   ├── model_loader.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── src/
│   ├── data_cleaning.py
│   ├── sqft_cleaning.py
│   ├── outlier_removal.py
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
│
├── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Outlier Detection & Removal
5. Model Training
6. Model Evaluation
7. Model Serialization (.pkl)
8. API Integration
9. Deployment

---

## 📊 Sample Prediction

### Input

| Feature   | Value     |
| --------- | --------- |
| Location  | Bangalore |
| Area      | 1200 sqft |
| Bedrooms  | 2         |
| Bathrooms | 2         |

### Output

```text
Estimated Property Price: ₹65,00,000
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/your-username/SmartPrice-AI.git
cd SmartPrice-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

## 🛠️ Technology Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* FastAPI
* Streamlit
* Joblib
* Render

---

## 📈 Future Enhancements

* XGBoost & Random Forest Models
* Improved Feature Engineering
* User Authentication
* Advanced Visualizations
* Real-Time Market Data Integration
* AWS Deployment

---

## 👨‍💻 Author

**Neeraj Mittal**

Data Science | Machine Learning | AI Enthusiast

GitHub: https://github.com/Neeraj5-mittal

---

## ⭐ Support

If you found this project helpful, consider giving it a star on GitHub.
