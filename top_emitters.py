import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'Carbon_(CO2)_Emissions_by_Country.csv'
data = pd.read_csv(file_path)

# Print basic info about the dataset
print("Data Overview:")
print(data.info())
print(data.head())

# Example Visualization: Top 10 Countries by Kilotons of CO2
top_emitters = data.groupby('Country')['Kilotons of Co2'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Emitters (by Kilotons of CO2):")
print(top_emitters)

top_emitters.plot(kind='bar', title='Top 10 Carbon Emitters')
plt.xlabel('Country')
plt.ylabel('Total Kilotons of CO2')
plt.show()