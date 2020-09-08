"""

The following is the 2nd .py file that reads the data.txt file and saves a new file
with continuous values. The new file is ContData.txt file

"""

import pandas as pd

# df = pd.read_csv("data.txt", index_col='Time')

df = pd.read_csv("data.txt")

print(df.describe())

cols_of_interest = ['Time',
                    'INDOOR Ambient Temp.',
                    'INDOOR Relative Humidity',
                    'INDOOR Air Velocity',
                    'INDOOR Mean Radiant Temp.',
                    'INDOOR Lumens',
                    'INDOOR CO2',
                    'OUTDOOR Ambient Temp.',
                    'OUTDOOR Relative Humidity',
                    'OUTDOOR Air Velocity',
                    'Metabolic Rate (last 15 mins.)',
                    'Metabolic Rate (last 1 hour)',
                    'Clothing Level',
                    'Clothing Level (+ Chair)',
                    'Current Thermostat COOLING Setpoint',
                    'Base Thermostat COOLING Setpoint',
                    'Current Thermostat HEATING Setpoint',
                    'Base Thermostat HEATING Setpoint',
                    'Net Clothing Change (recently)',
                    'Predicted Mean Vote (PMV)']

print(df.describe())

df2 = df[cols_of_interest]

df2.set_index('Time', inplace=True)

print(df2.describe())

df2.to_csv('ContData.txt', index=True)
