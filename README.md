# 🏥 Hospital Data Pipeline (Bronze → Silver → Gold)

A Python batch data pipeline that processes hospital data using a layered Medallion Architecture and generates analytical visualizations.

---

## 📌 Project Overview

This project implements a structured data pipeline that:

1. Ingests raw hospital data
2. Cleans and standardizes it
3. Detects medical anomalies
4. Generates analytical visualizations

The pipeline follows the **Bronze → Silver → Gold** architecture.

---

## 🏗 Architecture


data/ → bronze/ → silver/ → gold/ → visualizations/


### 🥉 Bronze Layer (Raw Ingestion)

- Reads raw source files from `data/`
- Stores exact copies in `bronze/`
- No transformations applied

Files:
- ehr.csv
- vitals.csv
- labs.csv

---

### 🥈 Silver Layer (Cleaning & Standardization)

Performs:

- Rename columns (patientId → patient_id)
- Convert UNIX timestamps to datetime
- Ensure numeric types (hr, ox, sys, dia, lab_value)
- Select latest vitals per patient
- Select latest lab result per test per patient
- Create unified `patient_master.csv`

Output:
- clean_vitals.csv
- clean_labs.csv
- patient_master.csv

---

### 🥇 Gold Layer (Anomaly Detection)

Detects anomalies using rule-based logic:

- High Heart Rate → HR > 120 bpm
- Low Oxygen → OX < 92%
- High Blood Pressure → SYS > 160 OR DIA > 100 mmHg

Output:
- anomalies.csv

---

### 📊 Visualization Layer

Generates charts using matplotlib:

1. Heart Rate Trend (hr_trend.png)
2. Oxygen Distribution (oxygen_distribution.png)
3. Anomaly Counts (anomaly_counts.png)

Saved inside:

visualizations/


---

## 🛠 Tech Stack

- Python 3.10+
- pandas
- numpy
- matplotlib
- pathlib
- json (if needed)

---

## 📁 Project Structure


Hospital Data Pipeline/
│
├── data/ # Input files
├── bronze/ # Raw ingested data
├── silver/ # Cleaned & standardized data
├── gold/ # Anomaly detection results
├── visualizations/ # Generated charts
│
├── src/
│ ├── bronze.py
│ ├── silver.py
│ ├── gold.py
│ ├── visualize.py
│ └── utils.py
│
├── main.py # Pipeline orchestrator
├── requirements.txt
└── README.md


---

## ▶️ How to Run

### 1️⃣ Clone Repository


git clone <your-repo-url>
cd Hospital-Data-Pipeline


### 2️⃣ Create Virtual Environment


python -m venv venv
venv\Scripts\activate (Windows)


### 3️⃣ Install Dependencies


pip install -r requirements.txt


### 4️⃣ Run Pipeline


python main.py


---

## 🔁 Re-runnable Behavior

The pipeline is fully idempotent:

- Always reads fresh input from `data/`
- Overwrites all outputs
- Regenerates visualizations
- No caching or state persistence

---

## 📈 Sample Outputs

After running:


bronze/
silver/
gold/
visualizations/


Generated outputs:

- silver/patient_master.csv
- gold/anomalies.csv
- visualizations/*.png

---

## 🎯 Key Concepts Demonstrated

- Medallion Architecture
- Batch Data Processing
- Data Cleaning & Transformation
- GroupBy & Aggregation
- Rule-Based Anomaly Detection
- Data Visualization
- Modular Python Design

---

## 👩‍💻 Author

Your Name  
Hospital Data Pipeline Project
✅ STEP 2 — Commit README to Git

Run:

git add README.md
git commit -m "Added professional README file"
git push