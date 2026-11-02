import joblib
import numpy as np
import streamlit as st



# Load Random Forest Model

@st.cache_resource
def load_model():

    try:
        model = joblib.load("model/rf_model.pkl")
        return model

    except Exception as e:
        st.error(f"Error loading AI model: {e}")
        return None


# Make Prediction

def predict_exposure(model, rf_power, frequency):

    if model is None:
        return None

    features = np.array([
        [
            rf_power,
            frequency
        ]
    ])

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]

    confidence = float(np.max(probabilities) * 100)

    class_names = model.classes_

    probability_dict = {}

    for cls, prob in zip(class_names, probabilities):
        probability_dict[cls] = round(prob * 100, 2)

    return {
        "prediction": prediction,
        "confidence": round(confidence, 2),
        "probabilities": probability_dict
    }



# Safety Recommendation

def get_recommendation(level):

    level = str(level).upper()

    if level == "SAFE":

        return (
            "🟢 Safe",
            "RF exposure is within acceptable limits."
        )

    elif level == "MODERATE":

        return (
            "🟡 Moderate",
            "Reduce exposure time and maintain a safe distance from RF sources."
        )

    elif level == "HAZARDOUS":

        return (
            "🔴 Hazardous",
            "High RF exposure detected. Increase your distance from the source and limit exposure immediately."
        )

    return (
        "Unknown",
        "No recommendation available."
    )