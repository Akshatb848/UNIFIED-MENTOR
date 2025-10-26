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

## 📊 Results (from sample runs)
> Results vary by dataset. In reported runs, accuracies ranged **~31–55%** with macro-F1 **~0.15–0.17** and weighted-F1 **~0.43–0.50** due to strong class imbalance and label subjectivity.

If your data is cleaner/more balanced, TF–IDF + linear models can approach **70–75%** accuracy with macro-F1 near **0.70**.

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
- If compute permits, move to **transformer-based** models (DistilBERT/BERT). These often add **5–10%** macro-F1 but are CPU/GPU intensive.

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
