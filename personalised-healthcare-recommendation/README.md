# 🩸 Blood Donation Prediction (Personalised Healthcare Recommendation project)

This folder was created for the "Personalised Healthcare Recommendation" internship brief, but the executed notebook and the included data are a **binary classification** task: predicting whether a past blood donor will donate again, using the **UCI Blood Transfusion Service Center** dataset. The prediction could be used to prioritise donor outreach (e.g. reminders); it does not generate medical or lifestyle recommendations.

> Earlier versions of this README described a dataset with Age, Gender, BMI, Blood Pressure, Smoking, Stress Level, etc., a Random Forest model, and ~81% accuracy. None of that matches `blood.csv` or the notebook outputs, so it has been replaced with what the notebook actually does.

---

## 📂 Contents

```
personalised-healthcare-recommendation/
├─ Blood_Donation_ProdReady_Final.ipynb    # executed notebook (all results below come from here)
├─ Blood_Donation_Research_Report.pdf      # report
├─ blood.csv                               # dataset (748 rows)
└─ README.md
```

---

## 📊 Dataset

**File:** `blood.csv`: 748 donors, 4 features + target, no missing values.

| Column | Description |
|--------|-------------|
| **Recency** | Months since last donation |
| **Frequency** | Total number of donations |
| **Monetary** | Total blood donated (c.c.); equals Frequency × 250 in 747 of 748 rows, so it is essentially redundant with Frequency |
| **Time** | Months since first donation |
| **Class** | Target: 1 = donated in the target month, 0 = did not |

Class balance: 570 × `0`, 178 × `1` (23.8% positive).

Split (stratified): train 561 / validation 93 / test 94.

---

## ⚙️ Pipeline

- **EDA:** per-feature histograms, correlation matrix.
- **Feature engineering** (`AddBloodFeatures` transformer): `avg_cc_per_donation`, `donation_rate` (Frequency / Time), `recency_ratio` (Recency / Time), `log1p` of Monetary, Frequency and Time.
- **Preprocessing:** median imputation + `StandardScaler` in a `ColumnTransformer`.
- **Models:** Logistic Regression (balanced), Random Forest (balanced_subsample), Gradient Boosting, a small Keras MLP, probability calibration (sigmoid / isotonic), and a soft-voting ensemble (RF + GB + LR).
- **Selection:** repeated stratified 5-fold × 3 CV on train, champion picked by macro-F1 on validation, then evaluated on test; decision-threshold sweep; permutation importance and partial-dependence plots.

---

## 🤖 Results

Repeated CV on train (macro-F1): LogReg 0.616 ± 0.042, Random Forest 0.606 ± 0.051, Gradient Boosting 0.619 ± 0.040.

Validation macro-F1: Gradient Boosting 0.669 (champion), Keras MLP 0.657.

**Test set (94 rows):**

| Model | Accuracy | ROC-AUC | PR-AUC | Macro-F1 | F1 (positive class) |
|-------|---------|---------|--------|----------|----------|
| Gradient Boosting (champion) | 0.745 | 0.715 | 0.404 | 0.604 | 0.368 |
| Calibrated GB (sigmoid) | 0.745 | 0.730 | 0.424 | 0.427 | 0.000 |
| Calibrated GB (isotonic) | 0.766 | 0.714 | 0.422 | 0.605 | 0.353 |
| **Soft vote (RF + GB + LR)** | **0.766** | **0.768** | **0.483** | **0.674** | **0.500** |

Best threshold-tuned result (GB, threshold 0.20): precision 0.447, recall 0.773, F1 0.567 for the positive class.

Permutation importance (macro-F1 drop): Recency 0.095, Frequency 0.071; Time and Monetary ≈ 0.

**Caveats.** The test set has 72 negatives out of 94, so always predicting "will not donate" would score **76.6% accuracy**, the same as the best model. Accuracy is therefore not informative here; ROC-AUC (0.77 at best) and positive-class F1 (0.50 at best) are the meaningful numbers. With only 94 test rows these estimates have wide uncertainty.

---

## 🛠 Tech Stack

| Category | Tools Used |
|---------|------------|
| Programming | Python 3.12 |
| Data Processing | pandas, NumPy |
| Visualization | Matplotlib |
| Modeling | scikit-learn; TensorFlow/Keras (optional MLP) |
| Persistence | joblib (artifacts written to `blood_prod_artifacts/`) |

The notebook was executed with Python 3.12.9, NumPy 2.0.2, pandas 2.2.3, scikit-learn 1.5.2, Matplotlib 3.8.4, TensorFlow 2.20.0.

---

## 📦 How to Run

```bash
git clone https://github.com/Akshatb848/UNIFIED-MENTOR.git
cd UNIFIED-MENTOR
pip install -r requirements.txt
cd personalised-healthcare-recommendation
jupyter notebook Blood_Donation_ProdReady_Final.ipynb
```

In the data-loading cell, change `DATA_PATH` (currently a local Windows path) to `"blood.csv"`, then run all cells. TensorFlow is optional; the MLP step is skipped if it is not installed.
