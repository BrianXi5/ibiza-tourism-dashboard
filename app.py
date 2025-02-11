import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from statsmodels.tsa.arima.model import ARIMA
import datetime

# Streamlit App Setup
st.title("Ibiza Daily Tourist Arrivals & Forecast")

# Simulated Data Collection (Replace with API Calls in the Future)
def fetch_tourist_data():
    date_rng = pd.date_range(start="2024-01-01", periods=90, freq='D')
    np.random.seed(42)  # For reproducibility
    
    flights_spain = np.random.randint(3000, 7000, size=len(date_rng))
    flights_international = np.random.randint(4000, 9000, size=len(date_rng))
    cruise_passengers = np.random.randint(500, 5000, size=len(date_rng))
    ferry_passengers = np.random.randint(2000, 6000, size=len(date_rng))
    
    data = pd.DataFrame({
        "Date": date_rng,
        "Flights_Spain": flights_spain,
        "Flights_International": flights_international,
        "Cruise_Passengers": cruise_passengers,
        "Ferry_Passengers": ferry_passengers
    })
    
    data["Total_Arrivals"] = data.sum(axis=1, numeric_only=True)
    data.set_index("Date", inplace=True)
    
    return data

# Fetch Data
data = fetch_tourist_data()

# Forecasting with ARIMA model (Basic Time-Series Prediction)
def forecast_tourism(data, forecast_days=30):
    model = ARIMA(data['Total_Arrivals'], order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=forecast_days)
    forecast_dates = [data.index[-1] + datetime.timedelta(days=i) for i in range(1, forecast_days+1)]
    return forecast, forecast_dates

forecast, forecast_dates = forecast_tourism(data)

# Plot Actual vs Forecasted Data
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data.index, data['Total_Arrivals'], label='Actual Arrivals')
ax.plot(forecast_dates, forecast, linestyle='dashed', label='Forecasted Arrivals", color='red')
ax.set_xlabel("Date")
ax.set_ylabel("Number of Tourists")
ax.set_title("Ibiza Daily Tourist Arrivals & Forecast")
ax.legend()
ax.grid()
plt.xticks(rotation=45)
st.pyplot(fig)
