
# RF Guardian Alert System


def classify_rf_level(rf_power):
    """
    Classify RF power into Safe, Moderate or Hazardous.
    """

    if rf_power < -65:
        return "SAFE"

    elif rf_power <= -45:
        return "MODERATE"

    else:
        return "HAZARDOUS"



# Alert Message


def get_alert(level):

    level = level.upper()

    if level == "SAFE":

        return {
            "icon": "🟢",
            "title": "Safe",
            "message": "RF exposure is within acceptable limits.",
            "color": "success"
        }

    elif level == "MODERATE":

        return {
            "icon": "🟡",
            "title": "Moderate",
            "message": "Monitor exposure and maintain a reasonable distance from RF sources.",
            "color": "warning"
        }

    elif level == "HAZARDOUS":

        return {
            "icon": "🔴",
            "title": "Hazardous",
            "message": "High RF exposure detected. Increase your distance from the RF source immediately.",
            "color": "error"
        }

    return {
        "icon": "⚪",
        "title": "Unknown",
        "message": "Unable to classify RF level.",
        "color": "info"
    }



# Streamlit Alert Display

def show_alert(st, rf_power):

    level = classify_rf_level(rf_power)

    alert = get_alert(level)

    if alert["color"] == "success":
        st.success(f"{alert['icon']} {alert['message']}")

    elif alert["color"] == "warning":
        st.warning(f"{alert['icon']} {alert['message']}")

    elif alert["color"] == "error":
        st.error(f"{alert['icon']} {alert['message']}")

    else:
        st.info(alert["message"])