# 🚔 AI Crime Hotspot Prediction

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-ML-EC4E20?style=flat-square)](https://xgboost.ai/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)]()

> 🚀 Geo-Spatial Machine Learning project to predict crime hotspots using real-world data

---

## 📌 Overview

This project predicts **crime-prone areas** using:
- 📍 Location data (Geo-Spatial)
- ⏱ Time features
- 🤖 Machine Learning models

---

## 📋 Table of Contents

- [Features](#-features)
- [Motivation](#-motivation)
- [System Architecture](#️-system-architecture)
- [Repository Structure](#-repository-structure)
- [Dataset Format](#-dataset-format)
- [Model Architecture](#-model-architecture)
- [Results](#-results)
- [Limitations & Future Work](#️-limitations--future-work)
- [Authors](#-authors)

---

## ✨ Features

- 🔥 Crime hotspot prediction using **XGBoost**
- 🗺 Spatial clustering using **H3 indexing**
- 📈 Time-series forecasting with **Prophet**
- 🧠 Explainability using **SHAP**
- 🌐 Interactive dashboard using **Streamlit**

---

## 🎯 Motivation

Urban crime patterns are complex and influenced by location, time, and external factors.

**Challenges:**
- ❌ Difficult to identify high-risk areas manually  
- ❌ Large-scale data is hard to analyze  
- ❌ Lack of real-time insights  

**Solution:**
- ✅ Predict crime hotspots using ML  
- ✅ Use geo-spatial indexing (H3)  
- ✅ Provide visual insights via dashboard  

---

## 🏗️ System Architecture
Data → Cleaning → Feature Engineering → H3 Indexing → Model → Prediction → Dashboard


---

## 📂 Repository Structure
project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── notebooks/
│ └── notebook.ipynb
│
├── data/
│ └── sample_data.csv
│
└── images/
├── shap.png
├── prophet.png
├── dashboard.png

---

## 📁 Dataset Format

- Source: Chicago Crime Dataset  
- Features:
  - Latitude, Longitude  
  - Year, Month, Hour  
  - Crime Type  
  - Arrest, Domestic  

Dataset is preprocessed and sampled for performance.

<img width="1355" height="589" src="https://github.com/user-attachments/assets/a83d49ff-304a-430b-93f7-daff2dd1fea3" />

---
## 🧠 Model Architecture
XGBoost for prediction
H3 indexing for spatial grouping
Prophet for time-series forecasting
SHAP for model explainability

--

## 📊 Results
📈 SHAP
<img width="865" src="https://github.com/user-attachments/assets/ea934934-e47e-4038-a9dd-aa07adf72fc1" />
🔮 Forecast
<img width="989" src="https://github.com/user-attachments/assets/b37ac7b7-ef73-4d88-ac5e-0680198fe1c3" />
🌐 Dashboard
<img width="1600" src="https://github.com/user-attachments/assets/8a602912-5fdd-4bd4-914c-0bb6de0c35cb" />

--

## ⚠️ Limitations & Future Work

Limitations:

-Dataset size constraints
-No real-time data

Future Work:

-Live data integration
-Deep learning models
-Cloud deployment

## Future Work:

Live data integration
Deep learning models
Cloud deployment

--

## 👨‍💻 Authors

Hriday Shah
