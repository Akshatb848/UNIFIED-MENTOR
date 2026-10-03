# Unified Mentor — Data Science Internship Projects

Four notebook-based data science projects completed during a data science internship at **Unified Mentor**: stock price forecasting, support-ticket text classification, blood-donation prediction, and web-traffic anomaly detection. Each sub-folder contains a Jupyter notebook, a PDF report and its own README. The results below are copied from the **executed notebook outputs**; nothing here has been re-run or tuned since.

## Projects

| Project | Problem | Approach | Dataset | Best result in the notebook |
|---|---|---|---|---|
| [`tcs-stock-data`](tcs-stock-data/) | Next-day TCS closing price | Lags, rolling stats, RSI/MACD/ATR; RidgeCV, Random Forest, XGBoost, CatBoost, small LSTM; 5-fold time-series CV + 20% hold-out | TCS daily OHLCV, 4,463 rows (2002–2021); CSV not included | **RidgeCV**: CV R² 0.989, RMSE 18.6; hold-out R² 0.996, MAPE 1.23%; directional accuracy **~51%** |
| [`csat-text-classification`](csat-text-classification/) | Predict customer-satisfaction rating from ticket text | TF-IDF (word + char n-grams) + LinearSVC / LogisticRegression / SGD, randomized search | Customer support tickets, 8,469 rows; CSV not included | Accuracy 0.32–0.55, **macro-F1 ≈ 0.16** (tuned SGD: acc 0.40, macro-F1 0.156) |
| [`personalised-healthcare-recommendation`](personalised-healthcare-recommendation/) | Predict whether a blood donor will donate again | Engineered ratios; LogReg, RF, Gradient Boosting, Keras MLP, calibration, soft voting | UCI Blood Transfusion (`blood.csv`), 748 rows, 4 features | Soft vote: **accuracy 0.766, macro-F1 0.674, ROC-AUC 0.768** (94-row test set) |
| [`Cybersecurity-Web-Threat-Detection`](Cybersecurity-Web-Threat-Detection/) | Flag suspicious web-traffic sessions | Traffic features + Isolation Forest (unsupervised) | CloudWatch web-traffic log, 282 rows; raw CSV not included | Isolation Forest flagged **15 / 282 (5.32%)**, set by `contamination=0.05`; no labels to evaluate |

## Limitations (read before citing these results)

- **TCS stock:** the high R² comes from next-day price being close to today's price (today's `Close` is a feature). Directional accuracy is ~51%, i.e. no better than chance. Tree models and CatBoost scored negative R²; the LSTM failed (MAPE 99%). No naive "tomorrow = today" baseline was computed.
- **CSAT:** 67% of labels are missing and kept as an `<NA>` class. Every model scores below the 67.3% majority-class baseline, and per-class F1 for ratings 1–5 is 0.03–0.12, so the text barely predicts the rating.
- **Blood donation:** the folder is named "personalised healthcare recommendation", but the work is binary donor-retention classification. The best test accuracy (76.6%) equals the "always predict no" baseline (72/94); ROC-AUC and positive-class F1 (0.50) are the meaningful metrics, and the test set is only 94 rows.
- **Cybersecurity:** all 282 rows carry the same label (`waf_rule`), so supervised training was skipped and detection quality cannot be measured. `Cybersecurity_Web_Threats_LSTM.ipynb` has **not been executed** and, despite its name, contains no LSTM code.
- Notebooks use hard-coded local or Colab data paths; three of the four raw datasets are not in the repo.

## How to open and run

The notebooks were executed with **Python 3.12** (3.12.9 / 3.12.12).

```bash
git clone https://github.com/Akshatb848/UNIFIED-MENTOR.git
cd UNIFIED-MENTOR
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

- `requirements.txt` lists everything the notebooks import. `xgboost`, `catboost` and `tensorflow` are optional; the notebooks skip those blocks if they are missing.
- `csat-text-classification/` also has its own pinned `requirements.txt` and `environment.yml`.
- Before running, set the data path in each notebook (`CSV_PATH`, `DATA_PATH`, or the CSAT prompt) to your local copy of the dataset. See each sub-project README for details.
- The `Cybersecurity_Web_Threats_Colab.ipynb` notebook is written for Google Colab (`/content/...` paths).
