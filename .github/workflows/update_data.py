import pandas as pd
import numpy as np

# Generate new simulated tourist data (Replace this with API data in the future)
date_rng = pd.date_range(start="2024-01-01", periods=90, freq='D')
np.random.seed(42)

flights_spain = np.random.randint(3000, 7000, size=len(date_rng))
flights_international = np.random.randint(4000, 9000, size=len(date_rng))
cruise_passengers = np.random.randint(500, 5000, size=len(date_rng))
ferry_passengers = np.random.randint(2000, 6000, size=len(date_rng))

# Create DataFrame
data = pd.DataFrame({
    "Date": date_rng,
    "Flights_Spain": flights_spain,
    "Flights_International": flights_international,
    "Cruise_Passengers": cruise_passengers,
    "Ferry_Passengers": ferry_passengers
})

data["Total_Arrivals"] = data.sum(axis=1, numeric_only=True)
data.set_index("Date", inplace=True)

# Save updated data to CSV
data.to_csv("ibiza_tourist_data.csv")

print("✅ Data updated successfully!")
