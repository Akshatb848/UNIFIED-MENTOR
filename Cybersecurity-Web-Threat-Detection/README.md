# Cybersecurity: Web Threat Detection

**Author:** Akshat Banga  
**Affiliation:** University of Southampton  
**Keywords:** Cybersecurity, Web Traffic Analysis, EDA, Isolation Forest, LSTM Autoencoder, Anomaly Detection, Feature Engineering  

---

## 📘 Overview
This repository presents a comprehensive analysis of **suspicious web traffic interactions** using:
- **Exploratory Data Analysis (EDA)**
- **Isolation Forest (Baseline Unsupervised Model)**
- **LSTM Autoencoder (Temporal Deep Learning Model)**

Initially, the project centered around **feature-engineered anomaly detection**, establishing theoretical grounding through entropy-driven outlier scoring.  
Subsequently, based on model evaluation insights and instructor expectations, the project was **extended to capture temporal attack evolution** via sequence-based deep learning.

---

## 🔍 Why This Project Matters
Traditional intrusion detection often fails when:
- Attack patterns are **low-frequency** (rare)
- Threat behavior is **dynamic or evolving**
- Labeled attack signatures are **not available**

This pipeline focuses on **unsupervised anomaly detection**, making it resilient in **zero-day** and **sparse-event** scenarios.

---

## 🧭 Methodology Overview

### 1) Data Source
CloudWatch-style web telemetry logs consisting of session-level network statistics:
- `bytes_in`, `bytes_out`, `session_duration_s`, `status`
- `src_ip`, `dst_ip`, and behavioral indicators such as `req_count` and `is_waf_rule`

### 2) Feature Engineering (Enhanced)
| Feature | Purpose |
|--------|---------|
| `in_rate_bps`, `out_rate_bps`, `total_rate_bps` | Throughput normalization |
| `in_out_ratio`, `bytes_diff` | Traffic asymmetry (exfiltration signal) |
| `req_per_min`, `bytes_per_sec` | Session behavior density |
| `hour`, `is_error` | Contextual metadata |

+ Additional **data consistency fixes** were implemented to:
- Correct missing values
- Unify time formats
- Prevent feature leakage across model stages

---

## 🧪 Baseline Model: Isolation Forest

### ✅ Improvements Done (Important)
| Issue Before Fixes | Resolution Applied |
|--------------------|------------------|
| Train/Test leakage due to random splits | **Time-aware chronological splitting** |
| Unstable anomaly scoring | **Threshold calibrated on TRAIN scores only** |
| Test set sometimes single-class | **Automatic stratified evaluation fallback** |
| Missing feature standardization | **RobustScaler with 5–95% quantile range** |

### 🎯 Model Outcome After Fixes
| Metric | Value | Interpretation |
|--------|-------|---------------|
| Train Anomaly Rate | **~5.33%** | Matches theoretical contamination target |
| Test Anomaly Rate | **~15.79%** | Indicates real anomaly clustering in later window |
| Precision | **High** | Model flags only confident anomalies |
| Recall | **Expectedly Low** | Sparse-event detection behavior |

### 🧾 Example Top Anomaly Observations
- High inbound HTTPS flows
- Asymmetric data transfer (exfiltration-like patterns)
- Bursty access sessions across repeating source IPs

---

## 🧠 Extended Model: LSTM Autoencoder (Temporal Analysis)
To model **attack evolution over time**, we introduced:
- Sliding window time-series sequences
- Encoder-decoder reconstruction loss scoring
- Dynamic anomaly thresholding

### 🎯 Advantage Over Isolation Forest
| Factor | Isolation Forest | LSTM Autoencoder |
|--------|-----------------|-----------------|
| Considers single session only | ✅ | ❌ |
| Considers sequence patterns | ❌ | ✅ |
| Detects gradual / low-rate attacks | Partial | Strong |
| Interpretability | High | Medium |

The LSTM model allowed detection of:
- **Slow-exfiltration**
- **Beaconing attempts**
- **Layered probe phases**

---

## 📊 Results Comparison

| Stage | Detection Strength | Key Insight |
|------|-------------------|-------------|
| **Before Fixes** | Weak interpretability, unstable score distribution | Threshold leakage impacted reliability |
| **After Isolation Forest Fixes** | Stronger anomaly precision, cleaner scoring | Outliers aligned with realistic threat behavior |
| **LSTM Autoencoder Model** | Captured temporal threat waves | Detected multi-step attacks invisible to static models |

---

## 🧾 Conclusion
This project validates that **robust feature engineering + leakage-safe unsupervised modeling** can reliably detect web anomalies even without labels.  
The introduction of the **LSTM Autoencoder** strengthens capability to detect **long-horizon adversarial behavior**.

---

## 🔮 Future Enhancements
- Ensemble scoring: IF + Autoencoder + One-Class SVM
- Real-time deployment on Kafka + Spark Streaming
- Dashboard visualization using Kibana or Grafana

---

## 🖥️ How to Run the Project

### On Google Colab
```python
DATA_PATH = "/content/processed_web_threats.csv"
