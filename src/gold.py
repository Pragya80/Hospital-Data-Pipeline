import pandas as pd


def run_gold():

    df = pd.read_csv("silver/patient_master.csv")

    anomalies = []

    for _, row in df.iterrows():

        if row["hr"] > 120:
            anomalies.append((row["patient_id"], "High Heart Rate"))

        if row["ox"] < 92:
            anomalies.append((row["patient_id"], "Low Oxygen"))

        if row["sys"] > 160 or row["dia"] > 100:
            anomalies.append((row["patient_id"], "High Blood Pressure"))

    anomaly_df = pd.DataFrame(anomalies, columns=["patient_id", "anomaly_type"])

    anomaly_df.to_csv("gold/anomalies.csv", index=False)

    print("[INFO] Gold layer completed.")