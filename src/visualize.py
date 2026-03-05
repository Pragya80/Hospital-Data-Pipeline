import pandas as pd
import matplotlib.pyplot as plt


def plot_hr_trend():

    df = pd.read_csv("silver/clean_vitals.csv")

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    for patient in df["patient_id"].unique():

        subset = df[df["patient_id"] == patient]

        plt.plot(subset["timestamp"], subset["hr"], label=f"Patient {patient}")

    plt.legend()

    plt.title("Heart Rate Trend")

    plt.xlabel("Time")

    plt.ylabel("Heart Rate")

    plt.savefig("visualizations/hr_trend.png")

    plt.clf()


def plot_oxygen_distribution():

    df = pd.read_csv("silver/clean_vitals.csv")

    plt.hist(df["ox"], bins=10)

    plt.axvline(92)

    plt.title("Oxygen Distribution")

    plt.xlabel("Oxygen Level")

    plt.ylabel("Frequency")

    plt.savefig("visualizations/oxygen_distribution.png")

    plt.clf()


def plot_anomaly_counts():

    df = pd.read_csv("gold/anomalies.csv")

    counts = df["anomaly_type"].value_counts()

    plt.bar(counts.index, counts.values)

    plt.title("Anomaly Counts")

    plt.xticks(rotation=45)

    plt.savefig("visualizations/anomaly_counts.png")

    plt.clf()


def run_visualizations():

    plot_hr_trend()

    plot_oxygen_distribution()

    plot_anomaly_counts()

    print("[INFO] Visualizations completed.")