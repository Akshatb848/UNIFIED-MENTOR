# 📈 TCS Stock Data – End-to-End Machine Learning Forecasting

This project focuses on forecasting **Tata Consultancy Services (TCS)** stock prices using a practical, well-structured data science workflow.  
The goal is to understand price behaviour, quantify patterns, and build a model that generalises reliably, avoiding overfitting and data leakage.

This folder includes:
- Executed **Jupyter Notebook** (outputs and figures embedded)
- Research-style **PDF report with figures**

---

## 📂 Project Structure

```
tcs-stock-data/
├─ TCS_Stock_Project (2).ipynb                 # executed notebook (all results below come from here)
├─ TCS_Stock_Analysis_Report_with_Figures.pdf  # report with figures
└─ README.md
```

The raw CSV (`TCS_stock_history.csv`, 4,463 daily rows, 2002-08-12 to 2021-09-30) is **not** included; the notebook reads it from a local path set in `CSV_PATH`.

---

## 🔍 Overview

The dataset used contains daily **Open, High, Low, Close, and Volume (OHLCV)** data for TCS.  
The workflow includes:

| Stage | Description |
|------|-------------|
| Data Pre-processing | Cleaning, date handling, forward filling missing values |
| Exploratory Data Analysis | Understanding returns, volatility, volume behaviour |
| Feature Engineering | Lags, rolling statistics, RSI, MACD, ATR, calendar effects |
| Modeling | RidgeCV (best performer), Random Forest, XGBoost, CatBoost, small LSTM |
| Evaluation | 5-fold `TimeSeriesSplit` CV + final chronological hold-out (last 20%); RMSE, MAE, MAPE, R², Directional Accuracy |

---

## 📊 Exploratory Data Analysis (EDA)

Figures are embedded in the notebook outputs and in `TCS_Stock_Analysis_Report_with_Figures.pdf` (there is no separate `images/` folder).

1. **Closing price trend** — overall movement of the stock over 2002–2021.
2. **Trading volume over time** — liquidity spikes and activity patterns.
3. **Distribution of daily returns** — heavy-tailed behaviour.
4. **Autocorrelation of returns (lags 1–20)** — dependencies in returns weaken quickly.

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

Target: next-day `Close`. Models compared with 5-fold `TimeSeriesSplit` (mean over folds, sorted by RMSE):

| Model | MAE | RMSE | MAPE % | R² | Directional Acc. % |
|---|---|---|---|---|---|
| **RidgeCV** ✅ best | 13.70 | 18.61 | 2.07 | **0.989** | 51.3 |
| Random Forest | 227.03 | 316.98 | 19.03 | −1.49 | 50.8 |
| XGBoost | 237.81 | 327.76 | 19.87 | −1.65 | 50.1 |
| CatBoost | 260.07 | 341.80 | 22.33 | −1.94 | 51.4 |

The tree ensembles have negative R², most likely because they cannot extrapolate beyond the price range seen in training, and the price trends strongly upward over time.

**Final hold-out (last 20% of the timeline, RidgeCV):** MAE 27.50, RMSE 38.05, MAPE 1.23%, R² 0.996, directional accuracy 51.2%.

**LSTM (Close-only, 30-day lookback, 12 epochs, unscaled inputs):** MAE 2283, RMSE 2354, MAPE 99.2% — effectively failed to fit and is not a usable model.

### 📈 Actual vs Predicted Comparison
The hold-out actual-vs-predicted plot for RidgeCV is in the notebook and PDF report.

### 🔥 Feature Importance (permutation importance, RidgeCV, hold-out)
Top features: current `Close`, `Close_lag_1`, `EMA_5`, `RollMin_5`, `EMA_20`, `RollMax_5`, `EMA_10`, `SMA_5` — i.e. the most recent price levels dominate.

---

## 📌 Results Summary

| Metric (RidgeCV) | CV mean | Hold-out |
|-------|-------------|---------|
| RMSE | 18.61 | 38.05 |
| MAE | 13.70 | 27.50 |
| MAPE | 2.07% | 1.23% |
| R² | 0.989 | 0.996 |
| Directional Accuracy | 51.3% | 51.2% |

**Interpretation.** The high R² mostly reflects that next-day price is very close to today's price (today's `Close` is a feature). Directional accuracy of ~51% is essentially a coin flip, so the model does **not** predict up/down moves better than chance. A naive "tomorrow = today" baseline was not computed in the notebook and would be the appropriate comparison.

---

## 🚀 How to Run

```bash
git clone https://github.com/Akshatb848/UNIFIED-MENTOR.git
cd UNIFIED-MENTOR/tcs-stock-data

pip install -r ../requirements.txt
jupyter lab
```

Set `CSV_PATH` in the second code cell to your local copy of `TCS_stock_history.csv`. The notebook was executed with Python 3.12.9, NumPy 2.0.2, pandas 2.2.3, scikit-learn 1.5.2; XGBoost, CatBoost and TensorFlow are optional (their blocks are skipped if not installed).

