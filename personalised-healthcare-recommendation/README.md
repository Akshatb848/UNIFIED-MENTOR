# 🩺 Personalized Healthcare Recommendation System

This project focuses on building an intelligent **personalized healthcare recommendation system** using patient health indicators such as **age, lifestyle, vitals, medical history**, and **risk factors**. The model predicts **personalized health recommendations** (e.g., dietary advice, physical activity suggestions, risk awareness) based on the user’s overall health profile.

This system can support **doctors, health coaches, fitness programs, and individuals** seeking tailored well-being guidance.

---

## ✅ Problem Statement

Healthcare recommendations often follow a **generalized approach**, ignoring individual lifestyle differences. This project aims to provide **personalized health suggestions** by analyzing:

- Physiological measures (Blood Pressure, Hemoglobin, BMI)
- Lifestyle behaviors (Smoking, Alcohol intake, Physical activity)
- Health history (Diabetes, Heart disease)
- Stress & diet quality scores

The objective is to **recommend actionable and individualized health advice** that supports better lifestyle decisions.

---

## 📂 Dataset Used

**File:** `blood.csv` (included in the repository)

| Feature | Description |
|--------|-------------|
| **Age** | Age of the individual |
| **Gender** | Male / Female |
| **Blood Pressure** | Systolic blood pressure (mmHg) |
| **Hemoglobin** | Blood Hemoglobin concentration (g/dL) |
| **Diabetes** | 1 = Diagnosed, 0 = No history |
| **Smoking** | 1 = Smoker, 0 = Non-smoker |
| **Alcohol Consumption** | Scale (1-5) representing frequency |
| **Physical Activity** | Hours of weekly exercise |
| **BMI** | Body Mass Index |
| **Heart Disease** | 1 = Present, 0 = Absent |
| **Diet Quality** | Score (1-5) based on nutritional habits |
| **Stress Level** | Score (1-5) |
| **Recommendation** | **Target output** → Personalized health advice category |

---

## 🔍 Exploratory Data Analysis (EDA)

### 1. Gender Distribution
Shows a balanced dataset → useful for unbiased predictions.

### 2. Age vs Recommendation Patterns
- Younger individuals receive more **preventive lifestyle** suggestions.
- Older individuals receive **heart & metabolic risk management** advice.

### 3. Correlation Heatmap (Important insights)
- **Blood Pressure** strongly correlates with **Heart Disease**.
- **BMI & Diet Quality** inversely correlate → higher BMI tends to indicate poor diet.
- **Stress Level** often correlates with **Smoking & Alcohol Intake**.

### 4. Lifestyle Risk Factors
| Risk Factor | High Risk (%) |
|------------|---------------|
| Smoking | ~30% |
| Alcohol Usage | ~35% |
| High Stress | ~40% |

These insights helped shape model features for final predictions.

---

## 🤖 Model Used

A **Random Forest Classifier** was trained because:

- Handles **mixed numerical and categorical data**
- Works well with **small-to-mid size datasets**
- Offers **feature importance analysis**

**Model Performance Metrics:**

| Metric | Score |
|--------|------|
| Accuracy | **~81%** |
| Macro F1 Score | **~78%** |

---

## 🛠 Tech Stack

| Category | Tools Used |
|---------|------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Modeling | Scikit-learn (Random Forest Classifier) |
| Deployment Ready | Jupyter Notebook / Streamlit (optional) |

---

## 📦 How to Run the Project

```bash
# Clone the repository
git clone https://github.com/Akshatb848/UNIFIED-MENTOR.git

# Navigate to the project folder
cd personalised-healthcare-recommendation

# Open Jupyter Notebook
jupyter notebook

# Run the notebook step-by-step
