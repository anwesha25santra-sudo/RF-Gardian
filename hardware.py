import random
import requests

ESP32_URL = "http://192.168.1.50/data"


def simulated_data():
    return {
        "RF_Power_dBm": round(random.uniform(-85, -30), 2),
        "Frequency_MHz": random.choice(
            [700, 900, 1800, 2100, 2400, 3500, 5200]
        ),
        "Source": "Simulation"
    }


def esp32_data():
    try:
        response = requests.get(
            ESP32_URL,
            timeout=2
        )

        response.raise_for_status()

        data = response.json()

        return {
            "RF_Power_dBm":
                data.get("RF_Power_dBm", -60),

            "Frequency_MHz":
                data.get("Frequency_MHz", 2400),

            "Distance_from_Source_m":
                data.get(
                    "Distance_from_Source_m",
                    10
                ),

            "Source": "ESP32"
        }

    except Exception:
        return simulated_data()


def get_live_data():
    return esp32_data()