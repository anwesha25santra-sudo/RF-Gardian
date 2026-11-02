
import pandas as pd
import streamlit as st


@st.cache_data
def load_dataset():

    try:
        return pd.read_csv(
            "dataset/Em_Radiation_Dataset_.csv"
        )

    except Exception:
        return pd.DataFrame()


def latest_reading(df):

    if df.empty:
        return None

    return df.iloc[-1]


def dashboard_metrics(df):

    latest = latest_reading(df)

    if latest is None:

        return {
            "rf_power": "N/A",
            "frequency": "N/A",
            "distance": "N/A",
            "temperature": "N/A",
            "environment": "N/A",
            "exposure": "N/A",
            "timestamp": "N/A"
        }

    return {
        "rf_power":
            latest.get("RF_Power_dBm", "N/A"),

        "frequency":
            latest.get("Frequency_MHz", "N/A"),

        "distance":
            latest.get(
                "Distance_from_Source_m",
                "N/A"
            ),

        "temperature":
            latest.get("Temperature_C", "N/A"),

        "environment":
            latest.get("Environment", "N/A"),

        "exposure":
            latest.get(
                "Exposure_Level",
                "N/A"
            ),

        "timestamp":
            latest.get(
                "Timestamp",
                "N/A"
            )
    }