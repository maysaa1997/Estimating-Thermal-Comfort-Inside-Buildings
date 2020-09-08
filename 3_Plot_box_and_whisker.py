"""

The following is the 3rd .py file that reads the ContData.txt file and draws box plots for each column

"""

import pandas as pd
import matplotlib as mp

df = pd.read_csv("ContData.txt")
print(df.describe())

# box and whisker Indoor Ambient Temp. plots
df['INDOOR Ambient Temp.'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker RH plots
df['INDOOR Relative Humidity'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Indoor Air Velocity plots
df['INDOOR Air Velocity'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Indoor Mean Radiant Temp. plots
df['INDOOR Mean Radiant Temp.'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Lumens plots
df['INDOOR Lumens'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Indoor CO2 plots
df['INDOOR CO2'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Outdoor Mean Radiant Temp. plots
df['OUTDOOR Ambient Temp.'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Indoor Mean Radiant Temp. plots
df['OUTDOOR Relative Humidity'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Outdoor Air Velocity plots
df['OUTDOOR Air Velocity'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker MR in last 15 min. plots
df['Metabolic Rate (last 15 mins.)'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker MR in last 1hr plots
df['Metabolic Rate (last 1 hour)'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Clothing level plots
df['Clothing Level'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Clothing level (+chair) plots
df['Clothing Level (+ Chair)'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Current Thermostat Cooling Setpoint plots
df['Current Thermostat COOLING Setpoint'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Base Thermostat Cooling Setpoint plots
df['Base Thermostat COOLING Setpoint'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Current Thermostat Heating Setpoint plots
df['Current Thermostat HEATING Setpoint'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Base Thermostat Heating Setpoint plots
df['Base Thermostat HEATING Setpoint'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker Net clothing change (recently) plots
df['Net Clothing Change (recently)'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()

# box and whisker PMV plots
df['Predicted Mean Vote (PMV)'].plot(kind='box', sharex=False, sharey=False)
mp.pyplot.show()
