import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'Carbon_(CO2)_Emissions_by_Country.csv'
data = pd.read_csv(file_path)

# Convert the Date column
data['Date'] = pd.to_datetime(data['Date'])

# Calculate global emissions trend over time
global_trend = data.groupby('Date')['Kilotons of Co2'].sum()

# Plot the global trend as a line plot
plt.figure(figsize=(10, 6))
global_trend.plot(kind='line', title='Global CO2 Emissions Over Time', marker='o')
plt.xlabel('Year')
plt.ylabel('Total Kilotons of CO2')
plt.grid()
plt.show()

# Plot global trend as a step plot
plt.figure(figsize=(10, 6))
plt.step(global_trend.index, global_trend, where='mid', color='green')
plt.title('Global CO2 Emissions Over Time (Step Plot)')
plt.xlabel('Year')
plt.ylabel('Total Kilotons of CO2')
plt.grid()
plt.show()