import plotly.express as px
import plotly.figure_factory as ff



# RF Power Trend

def rf_power_trend(df):

    fig = px.line(
        df,
        x="Timestamp",
        y="RF_Power_dBm",
        title="RF Power Trend",
        template="plotly_dark",
        markers=True
    )

    fig.update_layout(
        height=400,
        xaxis_title="Timestamp",
        yaxis_title="RF Power (dBm)",
        legend_title="",
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig



# Frequency Distribution

def frequency_distribution(df):

    fig = px.histogram(
        df,
        x="Frequency_MHz",
        nbins=30,
        title="Frequency Distribution",
        template="plotly_dark"
    )

    fig.update_layout(height=400)

    return fig



# Exposure Level Distribution

def exposure_distribution(df):

    counts = df["Exposure_Level"].value_counts().reset_index()
    counts.columns = ["Exposure_Level", "Count"]

    fig = px.bar(
    counts,
    x="Exposure_Level",
    y="Count",
    color="Exposure_Level",
    title="Exposure Level Distribution",
    template="plotly_dark"
)

    fig.update_layout(height=400)

    return fig



# Correlation Heatmap

def correlation_heatmap(df):

    corr = df[
        [
            "RF_Power_dBm",
            "Frequency_MHz",
            "Distance_from_Source_m",
            "Temperature_C",
            "WiFi_Count",
            "Bluetooth_Count"
        ]
    ].corr()

    fig = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.columns),
        colorscale="Viridis"
    )

    fig.update_layout(
        title="Correlation Heatmap",
        template="plotly_dark",
        height=550
    )

    return fig



# Environment Analysis

def environment_chart(df):

    fig = px.box(
        df,
        x="Environment",
        y="RF_Power_dBm",
        color="Environment",
        title="RF Power by Environment",
        template="plotly_dark"
    )

    fig.update_layout(height=450)

    return fig