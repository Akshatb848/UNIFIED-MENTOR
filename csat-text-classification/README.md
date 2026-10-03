# CSAT Text Classification (No-Transformers)

Traditional **TF–IDF + linear models** pipeline to predict **Customer Satisfaction Rating** from **support ticket text**.
The intention is to push classical ML to its practical ceiling without heavy transformer models, keeping compute simple.

## ✨ Features
- EDA: class distribution, ticket length distribution, optional crosstabs by channel/priority
- Text prep: combine `Ticket Subject` + `Ticket Description`, safe cleaning
- Features: TF–IDF (word 1–3, char 2–6), large max features (up to 120k each)
- Models: `LinearSVC`, `LogisticRegression (SAGA)`, `SGDClassifier`
- Class balancing: `class_weight='balanced'` (+ optional simple oversampling)
- Tuning: `RandomizedSearchCV` (StratifiedKFold, scoring = macro-F1), also tunes n-gram ranges
- Evaluation: macro/weighted F1, confusion matrix heatmaps, misclassification explorer
- Artifacts: saves best pipeline to `artifacts/csat_text_pipeline_tuned.joblib`

## 📁 Repository Structure
```
csat-text-classification/
├─ CSAT_Text_Enhanced_EDA_Tuning.ipynb   # main notebook
├─ requirements.txt
├─ environment.yml
├─ .gitignore
└─ LICENSE
```

## 🧰 Environment
Using **Python 3.12.12**.

### Conda (recommended)
```bash
conda env create -f environment.yml
conda activate csat-312
```

### pip
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Quickstart
1. Launch Jupyter:
   ```bash
   jupyter lab
   ```
2. Open `CSAT_Text_Enhanced_EDA_Tuning.ipynb`
3. Provide path to your CSV when prompted. Expected columns:
   - **`Ticket Description`** (text) — optionally **`Ticket Subject`** (auto-combined)
   - **`Customer Satisfaction Rating`** (target). If numeric 1–5 → auto-cast to categorical strings.
4. Run all cells. The notebook will:
   - Perform EDA
   - Train baselines and pick the best
   - Run expanded hyperparameter search
   - Save the tuned pipeline in `artifacts/`

## 📊 Results (from the executed notebook)
Data: 8,469 tickets × 17 columns; stratified 80/20 split (6,775 train / 1,694 validation). Labels: 6 classes, ratings `1`–`5` (~6.5% each) and **`<NA>` (67.3%, tickets with no rating, kept as its own class)**.

| Model | Accuracy | Macro-F1 | Weighted-F1 |
|---|---|---|---|
| LinearSVC (balanced) | 0.553 | 0.158 | 0.508 |
| LogisticRegression SAGA (balanced) | 0.316 | 0.161 | 0.373 |
| SGD hinge (balanced), selected by macro-F1 | 0.448 | 0.164 | 0.460 |
| SGD after `RandomizedSearchCV` (30 iters, best CV macro-F1 0.175) | 0.401 | 0.156 | 0.433 |

Interpretation: per-class F1 for ratings 1–5 is 0.03–0.12, i.e. the text carries almost no signal about the rating, and every model scores **below the 67.3% accuracy of always predicting `<NA>`**. Macro-F1 ≈ 0.16 is close to chance for 6 classes.

The notebook's original target of 70–75% accuracy / macro-F1 ≈ 0.70 was **not** reached, and there is no evidence in this repo that it is reachable on this dataset.

## 🧪 Inference with the Saved Pipeline
```python
import joblib, pandas as pd
pipe = joblib.load("artifacts/csat_text_pipeline_tuned.joblib")
texts = ["Subject text + description text here"]
pred = pipe.predict(texts)
print(pred)
```

## 📌 Notes
- Avoid committing raw CSVs / PII: keep data under `data/` which is in `.gitignore`.
- If classes are highly imbalanced, set `USE_OVERSAMPLE = True` in the notebook and re-run.

## 📈 Future Work
- Integrate **structured features** (e.g., `Ticket Channel`, `Ticket Priority`, SLA times) via `ColumnTransformer` alongside text.
- If compute permits, try **transformer-based** models (DistilBERT/BERT); not attempted in this project, and given how little signal the text carries here, gains are uncertain.

## 🛠️ GitHub: How to publish
```bash
cd csat-text-classification
git init
git add .
git commit -m "Initial commit: CSAT TF–IDF pipeline with EDA & tuning"
git branch -M main
git remote add origin https://github.com/USERNAME/csat-text-classification.git
git push -u origin main
```
Replace `USERNAME` with your GitHub handle.
