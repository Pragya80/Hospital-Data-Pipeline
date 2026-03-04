# Silver layer performs:

#✔ Data cleaning
#✔ Column standardization
#✔ Timestamp conversion
#✔ Latest vitals selection
#✔ Latest lab results
#✔ Patient master table creation

import pandas as pd


def clean_vitals():

    df = pd.read_csv("bronze/vitals.csv")

    df = df.rename(columns={
        "patientId": "patient_id"
    })

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    df["hr"] = pd.to_numeric(df["hr"], errors="coerce")
    df["ox"] = pd.to_numeric(df["ox"], errors="coerce")
    df["sys"] = pd.to_numeric(df["sys"], errors="coerce")
    df["dia"] = pd.to_numeric(df["dia"], errors="coerce")

    df.to_csv("silver/clean_vitals.csv", index=False)

    return df


def clean_labs():

    df = pd.read_csv("bronze/labs.csv")

    df = df.rename(columns={
        "patientId": "patient_id",
        "test": "lab_test",
        "value": "lab_value"
    })

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    df["lab_value"] = pd.to_numeric(df["lab_value"], errors="coerce")

    df.to_csv("silver/clean_labs.csv", index=False)

    return df


def create_patient_master():

    ehr = pd.read_csv("bronze/ehr.csv")
    vitals = pd.read_csv("silver/clean_vitals.csv")
    labs = pd.read_csv("silver/clean_labs.csv")

    vitals["timestamp"] = pd.to_datetime(vitals["timestamp"])
    labs["timestamp"] = pd.to_datetime(labs["timestamp"])

    latest_vitals = (
        vitals.sort_values("timestamp")
        .groupby("patient_id")
        .last()
        .reset_index()
    )

    latest_labs = (
        labs.sort_values("timestamp")
        .groupby(["patient_id", "lab_test"])
        .last()
        .reset_index()
    )

    labs_pivot = latest_labs.pivot(
        index="patient_id",
        columns="lab_test",
        values="lab_value"
    ).reset_index()

    master = ehr.merge(latest_vitals, on="patient_id", how="left")

    master = master.merge(labs_pivot, on="patient_id", how="left")

    master.to_csv("silver/patient_master.csv", index=False)


def run_silver():

    clean_vitals()
    clean_labs()
    create_patient_master()

    print("[INFO] Silver layer completed.")