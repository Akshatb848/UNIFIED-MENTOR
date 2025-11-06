# 📈 TCS Stock Data – End-to-End Machine Learning Forecasting

This project focuses on forecasting **Tata Consultancy Services (TCS)** stock prices using a practical, well-structured data science workflow.  
The goal is to understand price behaviour, quantify patterns, and build a model that generalises reliably, avoiding overfitting and data leakage.

This repository includes:
- Executed **Jupyter Notebook**
- Full **research-style PDF report with figures**
- Visual EDA insights and model evaluation outputs

---

## 📂 Project Structure


---

## 🔍 Overview

The dataset used contains daily **Open, High, Low, Close, and Volume (OHLCV)** data for TCS.  
The workflow includes:

| Stage | Description |
|------|-------------|
| Data Pre-processing | Cleaning, date handling, forward filling missing values |
| Exploratory Data Analysis | Understanding returns, volatility, volume behaviour |
| Feature Engineering | Lags, rolling statistics, RSI, MACD, ATR, calendar effects |
| Modeling | Ridge Regression, Random Forest, CatBoost (best performer) |
| Evaluation | RMSE, MAE, MAPE, R², Directional Accuracy |

---

## 📊 Exploratory Data Analysis (EDA)

### 1. TCS Closing Price Trend
Shows the overall movement of stock value over the observed period.

![Close Price](images/1_Close_Price.png)

### 2. Trading Volume Over Time
Captures liquidity spikes and market activity patterns.

![Volume](images/2_Trading_Volume.png)

### 3. Distribution of Daily Returns
Reveals heavy-tailed behaviour and volatility clusters.

![Returns Distribution](images/3_Returns_Distribution.png)

### 4. Autocorrelation of Returns (Lags 1–20)
Indicates that dependencies in returns weaken quickly → requiring engineered features.

![Autocorrelation](images/4_Autocorrelation.png)

---

## ⚙️ Feature Engineering

| Feature Type | Examples | Purpose |
|---|---|---|
| Lag Features | Close(t-1), Close(t-5), Close(t-10)… | Captures short-term price memory |
| Rolling Statistics | Rolling mean & std (5–200 days) | Captures smoothed trend + volatility |
| Technical Indicators | RSI(14), MACD, ATR(14) | Captures momentum & market behaviour |
| Time Features | Day of week, Month | Captures calendar effects |

---

## 🤖 Model Training & Selection

Models compared:
- **Ridge Regression** → baseline linear model
- **Random Forest Regressor**
- **CatBoost Regressor** ✅ **best performer**

### 📈 Actual vs Predicted Comparison

![Actual vs Predicted](images/5_Actual_vs_Predicted.png)

- Predictions follow overall trend well.
- Model is robust to noise, avoids overfitting sharp fluctuations.

### 🔥 Feature Importance (CatBoost)

![Feature Importance](images/6_Feature_Importance.png)

Key Influences:
- **Lagged returns**
- **Rolling means / rolling volatility**
- **RSI & MACD momentum indicators**

---

## 📌 Results Summary

| Metric | Performance |
|-------|-------------|
| RMSE | ~15–20 |
| MAE | Stable across test splits |
| Directional Accuracy | **~60%** (statistically meaningful in stock forecasting) |

This means the model **does not attempt unrealistic prediction precision**, but instead focuses on **trend understanding and directional correctness**, which is **valuable in finance**.

---

## 🚀 How to Run

```bash
git clone https://github.com/Akshatb848/UNIFIED-MENTOR.git
cd UNIFIED-MENTOR/tcs-stock-data

conda activate your_environment_name
jupyter lab

