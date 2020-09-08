__author__ = 'maysaa.khalil@utt.fr'
import common.data_container
import common.solar
import math
import common.processing.clasification



class DataContainer(common.data_container.DataContainer):


    def __init__(self, sample_time_in_secs=15 * 60, starting_stringdatetime='30/07/2012 00:15:00', ending_stringdatetime='01/08/2013 23:59:59'):
        common.data_container.DataContainer.__init__(self, sample_time_in_secs=sample_time_in_secs, starting_stringdatetime=starting_stringdatetime, ending_stringdatetime=ending_stringdatetime)
        self.register_database('Maysa', common.data_container.TruncatedLocalDatabase('Maysa-DB.sqlite3'))
        # self.register_database('weather', common.data_container.TruncatedLocalDatabase('weather.sqlite3'))
        # reference_variable_only = True

        self.add_continuous_variable('Maysa', 'INDOOR Ambient Temp', 10, remove_outliers=True, min_value=None, max_value=None, context='data')
        # if not reference_variable_only:
        self.add_continuous_variable('Maysa', 'INDOOR Relative Humidity', 20, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'INDOOR Air Velocity', 30, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'INDOOR_Mean_Radiant_Temp', 40, remove_outliers=True, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'INDOOR_Lumens', 50, remove_outliers=False, min_value=None, max_value=None, context='data')
        # if not reference_variable_only:
        self.add_continuous_variable('Maysa', 'INDOOR_CO2', 60, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'OUTDOOR_Ambient_Temp', 70, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'OUTDOOR_Relative_Humidity', 80, remove_outliers=False, min_value=None, max_value=None, context='data')


        self.add_continuous_variable('Maysa', 'OUTDOOR_Air_Velocity', 90, remove_outliers=False, min_value=None, max_value=None, context='data')
        # if not reference_variable_only:
        self.add_continuous_variable('Maysa', 'Metabolic_Rate (last 15 mins)', 100, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Metabolic_Rate (last 1 hour)', 110, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Clothing_Level', 120, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Clothing_Level (+ Chair)', 130, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Current_Thermostat_COOLING_Setpoint', 140, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Base_Thermostat_COOLING_Setpoint', 150, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Current_Thermostat_HEATING_Setpoint', 160, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Base_Thermostat_HEATING_Setpoint', 170, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Net_Clothing_Change_(recently)', 180, remove_outliers=False, min_value=None, max_value=None, context='data')
        self.add_continuous_variable('Maysa', 'Predicted_Mean_Vote_(PMV)', 190, remove_outliers=False, min_value=None, max_value=None, context='data')

if __name__ == '__main__':
    Maysa_data_container = DataContainer(sample_time_in_secs=15 * 60, starting_stringdatetime='30/07/2012 00:15:00', ending_stringdatetime='25/07/2013 19:00:00')
    print(Maysa_data_container)
    common.data_container.PlotterGUI(Maysa_data_container)