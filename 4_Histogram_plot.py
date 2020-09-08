"""

The following is the 4th .py file that reads the ContData.txt file and draws histogram for each column

"""

import pandas as pd
import matplotlib as mp

df = pd.read_csv("ContData.txt")

# box and whisker Indoor Ambient Temp. plots
df['INDOOR Ambient Temp.'].hist()
mp.pyplot.show()

# box and whisker RH plots
df['INDOOR Relative Humidity'].hist()
mp.pyplot.show()

# box and whisker Indoor Air Velocity plots
df['INDOOR Air Velocity'].hist()
mp.pyplot.show()

# box and whisker Indoor Mean Radiant Temp. plots
df['INDOOR Mean Radiant Temp.'].hist()
mp.pyplot.show()

# box and whisker Lumens plots
df['INDOOR Lumens'].hist()
mp.pyplot.show()

# box and whisker Indoor CO2 plots
df['INDOOR CO2'].hist()
mp.pyplot.show()

# box and whisker Outdoor Mean Radiant Temp. plots
df['OUTDOOR Ambient Temp.'].hist()
mp.pyplot.show()

# box and whisker Indoor Mean Radiant Temp. plots
df['OUTDOOR Relative Humidity'].hist()
mp.pyplot.show()

# box and whisker Outdoor Air Velocity plots
df['OUTDOOR Air Velocity'].hist()
mp.pyplot.show()

# box and whisker MR in last 15 min. plots
df['Metabolic Rate (last 15 mins.)'].hist()
mp.pyplot.show()

# box and whisker MR in last 1hr plots
df['Metabolic Rate (last 1 hour)'].hist()
mp.pyplot.show()

# box and whisker Clothing level plots
df['Clothing Level'].hist()
mp.pyplot.show()

# box and whisker Clothing level (+chair) plots
df['Clothing Level (+ Chair)'].hist()
mp.pyplot.show()

# box and whisker Current Thermostat Cooling Setpoint plots
df['Current Thermostat COOLING Setpoint'].hist()
mp.pyplot.show()

# box and whisker Base Thermostat Cooling Setpoint plots
df['Base Thermostat COOLING Setpoint'].hist()
mp.pyplot.show()

# box and whisker Current Thermostat Heating Setpoint plots
df['Current Thermostat HEATING Setpoint'].hist()
mp.pyplot.show()

# box and whisker Base Thermostat Heating Setpoint plots
df['Base Thermostat HEATING Setpoint'].hist()
mp.pyplot.show()

# box and whisker Net clothing change (recently) plots
df['Net Clothing Change (recently)'].hist()
mp.pyplot.show()

# box and whisker PMV plots
df['Predicted Mean Vote (PMV)'].hist()
mp.pyplot.show()
