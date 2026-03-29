# 📈 TCS Stock Data – End-to-End Machine Learning Forecasting

This project applies **data science and machine learning techniques** to forecast the stock prices of **Tata Consultancy Services (TCS)**.  
It demonstrates a full pipeline: **data collection, pre-processing, exploratory data analysis (EDA), feature engineering, model development, and evaluation**.  
The goal is to generate reliable short-term forecasts and identify key factors influencing stock price movements.

---

## 📂 Project Structure


---

## 🔍 Methodology

### 1. Data Pre-processing
- Loaded historical OHLCV data for TCS.  
- Handled missing values using forward fill.  
- Sorted chronologically to maintain leakage-free modeling.  

### 2. Exploratory Data Analysis (EDA)
- **Returns distribution**: heavy tails and volatility clustering observed.  
- **Autocorrelation**: weak beyond short lags, confirming near-randomness in returns.  
- **Trend analysis**: stock showed long-term upward trajectory with episodic volatility.  
- **Volume spikes**: correlated with market-moving events.  

### 3. Feature Engineering
- **Lag features**: 1–20 day lagged returns.  
- **Rolling statistics**: mean, std, min, max (5–200 day windows).  
- **Technical indicators**:
  - Relative Strength Index (RSI, 14-day)  
  - Moving Average Convergence Divergence (MACD)  
  - Average True Range (ATR, 14-day)  
- **Calendar effects**: day-of-week and month indicators.  

### 4. Model Development
- **Models tested**:  
  - Ridge Regression (linear baseline)  
  - Random Forest Regressor  
  - CatBoost Regressor (best performer)  

- **Validation strategy**:  
  - `TimeSeriesSplit` cross-validation (leakage-safe).  
  - Metrics: RMSE, MAE, MAPE, R², Directional Accuracy.  

---

## 📊 Results & Insights

- **CatBoost Regressor** delivered the best results:
  - RMSE: ~15–20  
  - MAE: consistently low, stable error  
  - Directional Accuracy: ~60% (statistically meaningful in finance)  

- **Key Influential Features**:
  - Lagged returns  
  - Rolling means/volatility  
  - RSI and MACD indicators  

- **Visual Findings**:
  - Predictions track overall trend well but underestimate sharp spikes.  
  - Residual distribution centered close to zero (reduced bias).  
  - Feature importance highlights technical + statistical signals.  

---

## 📑 Report

For an in-depth research-style explanation, refer to:  
📄 **`reports/TCS_Stock_Analysis_Report_with_Figures.pdf`**  

This includes:
- Abstract & Introduction  
- Methodology  
- Results with Matplotlib figures (returns distribution, autocorrelation, predictions, feature importance)  
- Conclusion & Future work  

---

## 🚀 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/Akshatb848/UNIFIED-MENTOR.git
   cd UNIFIED-MENTOR/tcs-stock-data
