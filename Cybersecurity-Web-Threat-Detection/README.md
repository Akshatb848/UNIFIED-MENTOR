# Cybersecurity: Web Threat Detection

**Author:** Akshat Banga  
**Context:** Data science internship project, Unified Mentor  
**Keywords:** Cybersecurity, Web Traffic Analysis, EDA, Feature Engineering, Isolation Forest, Anomaly Detection

---

## ⚠️ Status at a glance
- **Executed:** `Cybersecurity_Web_Threats_Colab.ipynb` (EDA, feature engineering, Isolation Forest) on a **282-row** CloudWatch web-traffic log.
- **Not executed:** `Cybersecurity_Web_Threats_LSTM.ipynb` has **no outputs**: none of its cells have been run. Despite its file name, its code is a refined **Isolation Forest** baseline; it contains **no LSTM or autoencoder code**.
- **No LSTM / LSTM Autoencoder results exist** in this repository. Earlier versions of this README described LSTM Autoencoder results and a "~15.79% test anomaly rate"; neither appears in any notebook output, so they have been removed.

---

## 📘 Overview
Exploratory analysis and **unsupervised anomaly detection** on suspicious web traffic interactions (AWS CloudWatch / VPC-flow style logs flagged by a WAF rule).

---

## 📂 Contents

```
Cybersecurity-Web-Threat-Detection/
├─ Cybersecurity_Web_Threats_Colab.ipynb   # executed: EDA + features + Isolation Forest
├─ Cybersecurity_Web_Threats_LSTM.ipynb    # NOT executed: refined Isolation Forest baseline (no LSTM despite the name)
├─ processed_web_threats.csv               # output of the Colab notebook (282 rows × 25 columns, incl. iso_anomaly)
├─ Cybersecurity_Web_Threats.pdf           # report
└─ README.md
```

---

## 🧭 Methodology (Colab notebook, executed)

### 1) Data Source
`CloudWatch_Traffic_Web_Attack.csv` (not included in the repo): **282 rows × 16 columns**: `bytes_in`, `bytes_out`, `creation_time`, `end_time`, `src_ip`, `src_ip_country_code`, `protocol`, `response.code`, `dst_port`, `dst_ip`, `rule_names`, `observation_name`, `source.meta`, `source.name`, `time`, `detection_types`.

### 2) Feature Engineering
| Feature | Purpose |
|--------|---------|
| `session_duration_s` | Session length from `creation_time` / `end_time` |
| `total_bytes`, `bytes_diff`, `in_out_ratio` | Volume and traffic asymmetry |
| `in_rate_bps`, `out_rate_bps`, `total_rate_bps` | Throughput normalisation |
| `hour` | Time-of-day context |

Model inputs: `bytes_in`, `bytes_out` plus the eight features above (10 total).

### 3) Supervised modelling: skipped
The intended label was `detection_types == "waf_rule"`, but **all 282 rows have `detection_types = waf_rule`**, so there is only one class. The notebook prints *"Supervised training skipped — not enough label diversity"*. No accuracy, precision, recall or ROC-AUC can be computed on this data.

### 4) Isolation Forest (unsupervised)
`StandardScaler` → `IsolationForest(n_estimators=300, contamination=0.05, random_state=42)`, fit on all 282 rows.

| Result | Value |
|--------|-------|
| Rows flagged as anomalous | **15 of 282 (5.32%)** |

The 5.32% rate is essentially set by the `contamination=0.05` parameter, not discovered by the model. With no labels, the flagged sessions have not been validated as real threats. A `bytes_in` vs `bytes_out` scatter of normal vs flagged sessions is in the notebook.

---

## 🧪 Refined Isolation Forest baseline (`_LSTM.ipynb`, not executed)
The second notebook contains code (not yet run) for:
- Chronological 80/20 train/test split
- `RobustScaler` (5–95% quantile range) + `IsolationForest` (300 trees, contamination 0.0532)
- Anomaly threshold calibrated on **train** scores only
- Stratified fallback evaluation if the test split is single-class
- A Top-15 anomalies table for triage and a `score_batch` helper for new data

Note: if `processed_web_threats.csv` is not found at the configured path, this notebook silently **generates 6,000 synthetic rows** instead. Check the "Loaded data from ..." message when you run it.

**No results are reported for this notebook because it has not been run.**

---

## 🔮 Possible Next Steps
- Run `Cybersecurity_Web_Threats_LSTM.ipynb` on the real processed data and report its outputs.
- Obtain labelled traffic (both benign and malicious) so detection quality can actually be measured.
- If sequence modelling is pursued, implement and evaluate an LSTM autoencoder; none exists yet.

---

## 🖥️ How to Run the Project

### On Google Colab
1. Upload `CloudWatch_Traffic_Web_Attack.csv` to `/content/` and open `Cybersecurity_Web_Threats_Colab.ipynb`.
2. Adjust `DATA_PATH` if needed and run all cells; it writes `/content/processed_web_threats.csv`.
3. For the refined baseline, upload `processed_web_threats.csv` and run `Cybersecurity_Web_Threats_LSTM.ipynb` with:
   ```python
   DATA_PATH = "/content/processed_web_threats.csv"
   ```

### Locally
```bash
pip install -r ../requirements.txt   # from the repository root requirements
jupyter lab
```
Set `DATA_PATH` to a local path (e.g. `processed_web_threats.csv` in this folder).
