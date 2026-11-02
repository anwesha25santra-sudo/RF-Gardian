import folium
from streamlit_folium import st_folium



# RF Heatmap

def create_heatmap(df):

    # Center map using average coordinates
    center_lat = df["Latitude"].mean()
    center_lon = df["Longitude"].mean()

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=12,
        tiles="OpenStreetMap"
    )

    for _, row in df.iterrows():

        rf = row["RF_Power_dBm"]

        if rf < -65:
            color = "green"

        elif rf <= -45:
            color = "orange"

        else:
            color = "red"

        popup = f"""
        <b>Environment:</b> {row['Environment']}<br>
        <b>RF Power:</b> {row['RF_Power_dBm']} dBm<br>
        <b>Frequency:</b> {row['Frequency_MHz']} MHz<br>
        <b>Distance:</b> {row['Distance_from_Source_m']} m<br>
        <b>Exposure:</b> {row['Exposure_Level']}
        """

        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=6,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
            popup=popup
        ).add_to(m)

    return m
 

# Display Heatmap

def show_heatmap(df):

    m = create_heatmap(df)

    st_folium(
        m,
        width=None,
        height=600
    )