# ai-crime-hotspot-prediction
AI-based crime hotspot prediction using geospatial ML, H3 indexing, and time-series forecasting

# 🚔 AI Crime Hotspot Prediction

## 📌 Overview
This project predicts crime-prone areas using machine learning, geospatial analysis, and time-series forecasting.

## 🧠 Features
- Spatial analysis using H3 indexing
- Machine learning models (XGBoost, Random Forest)
- Time-series forecasting using Prophet
- Model explainability using SHAP
- Interactive dashboard using Streamlit
- Heatmap visualization of crime hotspots

## 🗂 Dataset
Chicago Crime Dataset (sample included)

## ⚙️ Tech Stack
Python, Pandas, Scikit-learn, XGBoost, H3, Prophet, SHAP, Streamlit, Folium

## 📊 Results

### 🔥 Heatmap
![Heatmap](images/heatmap.png)

### 📈 SHAP Analysis
![SHAP](images/shap.png)

### 🔮 Forecast
![Prophet](images/prophet.png)

### 🌐 Dashboard
![Dashboard](images/dashboard.png)

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
