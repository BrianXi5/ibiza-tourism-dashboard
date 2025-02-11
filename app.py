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
    date_rng = pd.date_range(start=datetime.date.today() - datetime.timedelta(days=15), periods=30, freq='D')
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
def forecast_tourism(data, forecast_days=15):
    model = ARIMA(data['Total_Arrivals'], order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=forecast_days)
    forecast_dates = [data.index[-1] + datetime.timedelta(days=i) for i in range(1, forecast_days+1)]
    
    forecast_df = pd.DataFrame({
        "Date": forecast_dates,
        "Total_Arrivals": forecast
    })
    forecast_df.set_index("Date", inplace=True)
    
    return forecast_df

forecast_df = forecast_tourism(data)

# Combine past and future data
combined_data = pd.concat([data, forecast_df])

# Plot Staggered Bar Chart
fig, ax = plt.subplots(figsize=(12, 6))
combined_data.plot(kind='bar', stacked=True, ax=ax, width=0.8, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
ax.set_xlabel("Date")
ax.set_ylabel("Number of Tourists")
ax.set_title("Ibiza Daily Tourist Arrivals & Forecast")
plt.xticks(rotation=45)
st.pyplot(fig)

# Save data for future use
data.to_csv("ibiza_tourist_data.csv")
