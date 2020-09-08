"""

The following is the 4th .py file that reads the ContData.txt file and finds IQR values for each column
while ignoring NaN values

"""

# identify outliers with interquartile range
import pandas as pd
from numpy import nanpercentile


data = pd.read_csv("ContData.txt")

# calculate interquartile range
print("IQR Indoor Ambient Temp.")
q25, q75 = nanpercentile(data['INDOOR Ambient Temp.'], 25), nanpercentile(data['INDOOR Ambient Temp.'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['INDOOR Ambient Temp.'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['INDOOR Ambient Temp.'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR Indoor Relative Humidity")
q25, q75 = nanpercentile(data['INDOOR Relative Humidity'], 25), nanpercentile(data['INDOOR Relative Humidity'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['INDOOR Relative Humidity'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['INDOOR Relative Humidity'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR INDOOR Air Velocity")
q25, q75 = nanpercentile(data['INDOOR Air Velocity'], 25), nanpercentile(data['INDOOR Air Velocity'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['INDOOR Air Velocity'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['INDOOR Air Velocity'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR INDOOR Mean Radiant Temp.")
q25, q75 = nanpercentile(data['INDOOR Mean Radiant Temp.'], 25), nanpercentile(data['INDOOR Mean Radiant Temp.'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['INDOOR Mean Radiant Temp.'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['INDOOR Mean Radiant Temp.'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR INDOOR Lumens")
q25, q75 = nanpercentile(data['INDOOR Lumens'], 25), nanpercentile(data['INDOOR Lumens'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['INDOOR Lumens'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['INDOOR Lumens'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR INDOOR CO2")
q25, q75 = nanpercentile(data['INDOOR CO2'], 25), nanpercentile(data['INDOOR CO2'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['INDOOR CO2'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['INDOOR CO2'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR OUTDOOR Ambient Temp.")
q25, q75 = nanpercentile(data['OUTDOOR Ambient Temp.'], 25), nanpercentile(data['OUTDOOR Ambient Temp.'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['OUTDOOR Ambient Temp.'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['OUTDOOR Ambient Temp.'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR OUTDOOR Relative Humidity")
q25, q75 = nanpercentile(data['OUTDOOR Relative Humidity'], 25), nanpercentile(data['OUTDOOR Relative Humidity'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['OUTDOOR Relative Humidity'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['OUTDOOR Relative Humidity'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR OUTDOOR Air Velocity")
q25, q75 = nanpercentile(data['OUTDOOR Air Velocity'], 25), nanpercentile(data['OUTDOOR Air Velocity'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['OUTDOOR Air Velocity'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['OUTDOOR Air Velocity'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("IQR Metabolic Rate (last 15 mins.)")
q25, q75 = nanpercentile(data['Metabolic Rate (last 15 mins.)'], 25), nanpercentile(data['Metabolic Rate (last 15 mins.)'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Metabolic Rate (last 15 mins.)'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Metabolic Rate (last 15 mins.)'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Metabolic Rate (last 1 hour)")
q25, q75 = nanpercentile(data['Metabolic Rate (last 1 hour)'], 25), nanpercentile(data['Metabolic Rate (last 1 hour)'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Metabolic Rate (last 1 hour)'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Metabolic Rate (last 1 hour)'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Clothing Level")
q25, q75 = nanpercentile(data['Clothing Level'], 25), nanpercentile(data['Clothing Level'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Clothing Level'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Clothing Level'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Clothing Level (+ Chair)")
q25, q75 = nanpercentile(data['Clothing Level (+ Chair)'], 25), nanpercentile(data['Clothing Level (+ Chair)'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Clothing Level (+ Chair)'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Clothing Level (+ Chair)'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Current Thermostat COOLING Setpoint")
q25, q75 = nanpercentile(data['Current Thermostat COOLING Setpoint'], 25), nanpercentile(data['Current Thermostat COOLING Setpoint'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Current Thermostat COOLING Setpoint'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Current Thermostat COOLING Setpoint'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Base Thermostat COOLING Setpoint")
q25, q75 = nanpercentile(data['Base Thermostat COOLING Setpoint'], 25), nanpercentile(data['Base Thermostat COOLING Setpoint'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Base Thermostat COOLING Setpoint'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Base Thermostat COOLING Setpoint'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Current Thermostat HEATING Setpoint")
q25, q75 = nanpercentile(data['Current Thermostat HEATING Setpoint'], 25), nanpercentile(data['Current Thermostat HEATING Setpoint'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Current Thermostat HEATING Setpoint'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Current Thermostat HEATING Setpoint'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Base Thermostat HEATING Setpoint")
q25, q75 = nanpercentile(data['Base Thermostat HEATING Setpoint'], 25), nanpercentile(data['Base Thermostat HEATING Setpoint'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Base Thermostat HEATING Setpoint'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Base Thermostat HEATING Setpoint'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Net Clothing Change (recently)")
q25, q75 = nanpercentile(data['Net Clothing Change (recently)'], 25), nanpercentile(data['Net Clothing Change (recently)'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Net Clothing Change (recently)'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Net Clothing Change (recently)'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))


# calculate interquartile range
print("*******************************")
print("Predicted Mean Vote (PMV)")
q25, q75 = nanpercentile(data['Predicted Mean Vote (PMV)'], 25), nanpercentile(data['Predicted Mean Vote (PMV)'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['Predicted Mean Vote (PMV)'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['Predicted Mean Vote (PMV)'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))