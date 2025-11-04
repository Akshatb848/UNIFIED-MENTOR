# Cybersecurity: Web Threat Detection

**Author:** Akshat Banga  
**Affiliation:** University of Southampton  
**Keywords:** Cybersecurity, Web Traffic Analysis, EDA, Isolation Forest, Anomaly Detection, Feature Engineering  

---

## 📘 Overview
This repository presents a comprehensive data-driven and theoretical analysis of **suspicious web traffic interactions** using **Exploratory Data Analysis (EDA)** and **Isolation Forest-based anomaly detection**.  
The project builds a robust feature-engineered model to identify irregular web session patterns from CloudWatch-like telemetry data.  
It integrates statistical theory, information entropy principles, and unsupervised learning paradigms to demonstrate the interpretability and mathematical soundness of network anomaly detection systems.

---

## 🧩 Research Motivation
Modern web infrastructures generate massive telemetry logs from virtual networks, often containing latent indicators of cyber threats such as DDoS, injection attempts, or reconnaissance.  
Traditional supervised intrusion detection systems fail in zero-day or low-frequency anomalies.  
This study employs **feature engineering + unsupervised modeling** to address this gap, guided by:
- Heavy-tailed network traffic theory  
- Entropy-based anomaly detection (Isolation Forest)  
- Empirical EDA on byte-level and rate-based session attributes  

---

## ⚙️ Methodology

### 1. Data Source
- **Dataset:** CloudWatch Web Traffic Logs (282 records × 16 columns)
- **Core Attributes:** `bytes_in`, `bytes_out`, `protocol`, `src_ip_country_code`, `session_duration_s`, `detection_types`

### 2. Data Preprocessing
- Timestamp parsing (`creation_time`, `end_time`)  
- Normalization and schema standardization  
- Missing value handling and type conversion  

### 3. Feature Engineering
Derived variables for analytical richness:
| Feature | Description |
|----------|-------------|
| `session_duration_s` | Session lifetime (end_time - creation_time) |
| `total_bytes` | Sum of inbound and outbound bytes |
| `in_out_ratio` | Asymmetry measure between incoming and outgoing traffic |
| `in_rate_bps`, `out_rate_bps`, `total_rate_bps` | Normalized transmission rates |
| `hour` | Temporal feature representing time of day |

### 4. Anomaly Detection
- **Model:** Isolation Forest (Liu et al., 2008)  
- **Parameters:** 300 estimators, contamination = 0.05  
- **Output:** Binary anomaly classification (`iso_anomaly` = 1 indicates anomalous session)

---

## 📊 Exploratory Data Analysis (EDA)

Key findings from distributional and correlation analysis:

| Observation | Theoretical Link |
|--------------|------------------|
| Heavy-tailed distributions of `bytes_in` and `bytes_out` | Pareto-like network traffic behavior |
| High correlation among rate-based features | Multicollinearity in throughput space |
| Bursty, clustered temporal patterns | Non-Poissonian request arrivals |
| 5.32% anomaly rate detected | Aligns with sparse-event models in cybersecurity |

### Figures
1. **Distribution of Bytes In** — Right-skewed heavy tail  
2. **Distribution of Bytes Out** — Asymmetric flow pattern  
3. **Protocol Frequency** — HTTPS dominance  
4. **Top Source Country Codes** — US & CA major contributors  
5. **Temporal Plots** — Bursty inbound/outbound byte progression  
6. **Correlation Heatmap** — High linear dependence among traffic rates  
7. **Anomaly Scatterplot** — Outliers indicating suspicious sessions  

---

## 🧠 Theoretical Analysis
The project mathematically models anomaly detection through:
- **Heavy-Tailed Distribution Theory:** Describing byte flow irregularities  
- **Covariance Matrix (ρ):** Quantifying multicollinearity in rate variables  
- **Isolation Forest Formulation:**
  \[
  s(x, n) = 2^{-E(h(x))/c(n)}
  \]
  where *E(h(x))* is the expected path length, and *c(n)* represents average path depth for *n* samples.  
  Lower values of *E(h(x))* correspond to higher anomaly probability, aligning with entropy minimization principles.

---

## 📈 Results Summary
| Metric | Value | Interpretation |
|---------|--------|----------------|
| **Dataset Size** | 282 rows × 25 features | Moderate, structured telemetry data |
| **Anomaly Rate** | 5.32% (15 sessions) | Within theoretical bounds |
| **Dominant Protocol** | HTTPS | Secure web interactions dominate |
| **Strongest Correlation** | `total_rate_bps` ↔ `in_rate_bps` (ρ ≈ 0.92) | Confirms rate dependency |

---

## 📚 Conclusion
The integration of **feature engineering**, **EDA**, and **Isolation Forest theory** validated the hypothesis that high-volume network logs exhibit statistically predictable anomaly distributions.  
The model achieves interpretability through mathematically grounded metrics and aligns with theoretical network burst dynamics.

### 🔮 Future Work
- Implement LSTM Autoencoders for temporal sequence anomaly detection  
- Extend feature set with rolling-window rates and entropy-based indicators  
- Develop a hybrid **Isolation-GAN** for semi-supervised threat modeling  

---

## 🧾 References
1. F. T. Liu, K. M. Ting, and Z.-H. Zhou, *“Isolation Forest,”* Proc. IEEE ICDM, 2008.  
2. W. McKinney, *“Data Structures for Statistical Computing in Python,”* PyData Conf., 2010.  
3. C. Bishop, *Pattern Recognition and Machine Learning,* Springer, 2006.  
4. AWS Documentation, *CloudWatch Logs and Network Telemetry Insights,* 2024.  

---

## 🖥️ How to Run the Project

### ▶ On Google Colab
1. Upload the following files:
   - `Cybersecurity_Web_Threats_Colab.ipynb`
   - `CloudWatch_Traffic_Web_Attack.csv`
2. Adjust the dataset path:
   ```python
   DATA_PATH = "/content/CloudWatch_Traffic_Web_Attack.csv"
