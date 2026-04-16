import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

st.set_page_config(page_title="Sales Forecasting System", layout="wide")

st.title("📈 Time-Series Forecasting System")

st.sidebar.header("⚙️ Settings")

forecast_days = st.sidebar.slider(
    "Forecast Horizon (Days)",
    min_value=30,
    max_value=180,
    value=90
)

file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("📊 Raw Data")
    st.dataframe(df.head())

    st.sidebar.subheader("📌 Select Columns")

    date_col = st.sidebar.selectbox("Select Date Column", df.columns)
    target_col = st.sidebar.selectbox("Select Target Column", df.columns)

    if date_col == target_col:
        st.error("❌ Date and Target columns must be different.")
        st.stop()

    df[date_col] = pd.to_datetime(df[date_col], dayfirst=True, errors='coerce')
    df = df.dropna(subset=[date_col, target_col])

    df[target_col] = pd.to_numeric(df[target_col], errors='coerce')
    df = df.dropna(subset=[target_col])

    df = df.groupby(date_col)[target_col].sum().reset_index()
    df.rename(columns={date_col: 'ds', target_col: 'y'}, inplace=True)

    st.subheader("✅ Processed Data")
    st.dataframe(df.head())

    if len(df) < 2:
        st.error("❌ Not enough valid data after processing. Please check your file or column selection.")
        st.stop()

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(df)

    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)

    st.subheader("📈 Forecast vs Actual")

    fig, ax = plt.subplots()

    ax.plot(df['ds'], df['y'], label="Actual")
    ax.plot(forecast['ds'], forecast['yhat'], label="Forecast")

    ax.set_xlabel("Date")
    ax.set_ylabel("Values")
    ax.legend()

    st.pyplot(fig)

    st.subheader("📊 Model Insight")

    last_actual = df['y'].iloc[-1]
    future_forecast = forecast[forecast['ds'] > df['ds'].max()]
    next_pred = future_forecast.iloc[0]['yhat']

    growth = ((next_pred - last_actual) / last_actual) * 100

    col1, col2, col3 = st.columns(3)

    col1.metric("Last Actual", f"{last_actual:,.0f}")
    col2.metric("Next Forecast", f"{next_pred:,.0f}", delta=f"{growth:.2f}%")
    col3.metric("Growth %", f"{growth:.2f}%")

    if growth > 0:
        st.success("📈 Sales are expected to increase.")
    elif growth < 0:
        st.warning("📉 Sales are expected to decline.")
    else:
        st.info("⚖️ Sales are expected to remain stable.")

    st.subheader("📋 Forecast Data")

    st.dataframe(
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(20)
    )

    st.subheader("📉 Trend & Seasonality")

    fig2 = model.plot_components(forecast)
    st.pyplot(fig2)

else:
    st.info("👆 Upload a CSV file to start forecasting.")