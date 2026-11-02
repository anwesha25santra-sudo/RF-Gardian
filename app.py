import streamlit as st
from styles import load_css
from utils import load_dataset, dashboard_metrics
from ai_model import load_model
from hardware import get_live_data

from charts import (
    rf_power_trend,
    frequency_distribution,
    exposure_distribution,
    correlation_heatmap,
    environment_chart
)

from heatmap import show_heatmap
from alerts import show_alert


# Page Configuration


st.set_page_config(
    page_title="RF Guardian",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()


# Load Resources


df = load_dataset()

model = load_model()


# Sidebar

st.sidebar.image("images/logo.jpeg", width=100)

st.sidebar.title("📡 RF Guardian")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "📡 Live Monitoring",

        "🤖 AI Prediction",

        "📊 Data Analysis",

        "🌍 RF Heatmap",

        "🚨 Alerts",

        "ℹ About"

    ]

)



st.sidebar.markdown("---")

st.sidebar.success("System Ready")

st.sidebar.write("AI Model: Random Forest")

st.sidebar.write("Version 1.0")


# Header


st.title("📡 RF Guardian")

st.caption(
    "AI-Based RF Radiation Detection & Early Warning System"
)

st.divider()


# Dashboard


if page == "🏠 Dashboard":

    metrics = dashboard_metrics(df)

    st.subheader("System Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "RF Power",
        f"{metrics['rf_power']} dBm"
    )

    c2.metric(
        "Frequency",
        f"{metrics['frequency']} MHz"
    )

    c3.metric(
        "Exposure",
        metrics["exposure"]
    )

    c4.metric(
        "Temperature",
        f"{metrics['temperature']} °C"
    )

    st.divider()

    a, b = st.columns(2)

    with a:

        st.metric(
            "Environment",
            metrics["environment"]
        )

    with b:

        st.metric(
            "Distance",
            f"{metrics['distance']} m"
        )

    st.divider()

    st.plotly_chart(

        rf_power_trend(df),

        use_container_width=True

    )

    show_alert(

        st,

        metrics["rf_power"]

    )


# Live Monitoring

elif page == "📡 Live Monitoring":

    st.subheader("📡 Live RF Monitoring")

    live = get_live_data()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "RF Power",
        f"{live['RF_Power_dBm']} dBm"
    )

    c2.metric(
        "Frequency",
        f"{live['Frequency_MHz']} MHz"
    )

    c3.metric(
        "Distance",
        f"{live['Distance_from_Source_m']} m"
    )

    c4.metric(
        "Source",
        live["Source"]
    )

    st.divider()

    show_alert(
        st,
        live["RF_Power_dBm"]
    )

    st.info(
        "Simulation mode will automatically switch to ESP32 when hardware is connected."
    )



# AI Prediction


elif page == "🤖 AI Prediction":

    st.subheader("🤖 AI Prediction")

    rf_power = st.slider(
        "RF Power (dBm)",
        -100,
        0,
        -55
    )


    frequency = st.selectbox(

        "Frequency (MHz)",

        [
            700,
            900,
            1800,
            2100,
            2400,
            3500,
            5200
        ]
    )

    st.divider()

    if st.button("Predict Exposure Level"):

        from ai_model import (
            predict_exposure,
            get_recommendation
        )

        result = predict_exposure(
            model,
            rf_power,
            frequency
        )

        if result is None:

            st.error("Unable to load AI model.")

        else:

            st.success(
                f"Prediction : {result['prediction']}"
            )

            st.metric(
                "Confidence",
                f"{result['confidence']} %"
            )

            st.subheader("Class Probabilities")

            st.json(
                result["probabilities"]
            )

            title, recommendation = get_recommendation(
                result["prediction"]
            )

            st.info(
                f"{title}\n\n{recommendation}"
            )


# Data Analysis


elif page == "📊 Data Analysis":

    st.subheader("📊 Data Analysis")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "RF Trend",
            "Frequency",
            "Exposure",
            "Correlation",
            "Environment"
        ]
    )

    with tab1:
        st.plotly_chart(
            rf_power_trend(df),
            use_container_width=True
        )

    with tab2:
        st.plotly_chart(
            frequency_distribution(df),
            use_container_width=True
        )

    with tab3:
        st.plotly_chart(
            exposure_distribution(df),
            use_container_width=True
        )

    with tab4:
        st.plotly_chart(
            correlation_heatmap(df),
            use_container_width=True
        )

    with tab5:
        st.plotly_chart(
            environment_chart(df),
            use_container_width=True
        )



# RF Heatmap


elif page == "🌍 RF Heatmap":

    st.subheader("🌍 RF Radiation Heatmap")

    show_heatmap(df)



# Alerts


elif page == "🚨 Alerts":

    st.subheader("🚨 Current RF Status")

    metrics = dashboard_metrics(df)

    show_alert(
        st,
        metrics["rf_power"]
    )

    st.divider()

    st.write("### Latest Reading")

    st.dataframe(
        df.tail(10),
        use_container_width=True
    )



# About


elif page == "ℹ About":

    st.subheader("About RF Guardian")

    st.markdown("""
### 📡 RF Guardian

An AI-Based RF Radiation Detection and Early Warning System.

---

### Objective

Monitor RF radiation levels, classify exposure using Artificial Intelligence,
and provide early warning alerts.

---

### AI Model

Random Forest Classifier

---

### Hardware

- ESP32
- AD8318 RF Detector

---

### Technologies

- Python
- Streamlit
- Scikit-learn
- Plotly
- Folium
- Pandas
- NumPy

---

### Features

✅ Live Monitoring

✅ AI Prediction

✅ RF Heatmap

✅ Data Analysis

✅ Alerts

---
""")

