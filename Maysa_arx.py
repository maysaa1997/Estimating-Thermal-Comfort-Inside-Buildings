__author__ = 'stephane.ploix@g-scop.grenoble-inp.fr'

import app.data_container

import common.processing.arx

# model configuration

class ARX ():

    def __init__(self,sample_time_in_minutes: float, starting_stringdatetime: str, ending_stringdatetime: str ):
        self.data_container = app.data_container.DataContainer(sample_time_in_secs=sample_time_in_minutes * 60, starting_stringdatetime =starting_stringdatetime , ending_stringdatetime = ending_stringdatetime)
    #     self.input_labels = ('INDOOR Relative Humidity', 'INDOOR Air Velocity', 'INDOOR_Mean_Radiant_Temp', 'INDOOR_CO2', 'Metabolic_Rate (last 15 mins)','Clothing_Level')
    #
    # def get_input_labels(self):
    #     return self.input_labels
    def model_(self, pset,input_labels):
        # input_labels = ('INDOOR Relative Humidity', 'INDOOR Air Velocity', 'INDOOR_Mean_Radiant_Temp', 'INDOOR_CO2', 'Metabolic_Rate (last 15 mins)','Clothing_Level')
        # input_labels = ('INDOOR Relative Humidity', 'INDOOR_Mean_Radiant_Temp','INDOOR Ambient Temp')

        # input_labels = ('total_power_elec_delivered_nt_W_2_REF', 'SetpointBoilerTemperature_REF', 'Tout', 'phi_sun_horizontal', 'phi_sun_north', 'phi_sun_south', 'phi_sun_west', 'phi_sun_east', 'WindSpeed','CurrentHumidity_REF')
        output_label = 'Predicted_Mean_Vote_(PMV)'

        offset = False
        minimum_input_delay = 2
        inputs_maximum_delays = 3
        ouput_maximum_delay = 2

        # training data

        training_starting_stringdatetime = '30/07/2012 01:00:00'
        training_ending_stringdatetime = '31/12/2012 0:00:00'

        # validation data

        validation_starting_stringdatetime = '01/01/2013 0:00:00'
        validation_ending_stringdatetime = '29/07/2013 19:33:26'

        # display

        correlation = False
        pole_zeros = False


        ################################################

        sample_time_in_minutes = 15

        cycle = 5 * 60 / sample_time_in_minutes  # 24 * 60 / sample_time_in_minutes OR None

        print('TRAINING')

        data_container = app.data_container.DataContainer(sample_time_in_secs=sample_time_in_minutes * 60, starting_stringdatetime=training_starting_stringdatetime, ending_stringdatetime=training_ending_stringdatetime)
        print(data_container)
        inputs = [data_container.get_variable_data(data_label) for data_label in input_labels]
        for i in range (len (input_labels)):
            print ('data label ' , input_labels[i])
            inputs[i] = pset.val(input_labels[i])


        print ("inputs ", inputs)
        output = data_container.get_variable_data(output_label)
        print("outputs ", output)
        arx_model = common.processing.arx.Arx(minimum_input_delay=minimum_input_delay, inputs_maximum_delays=inputs_maximum_delays, output_maximum_delay=ouput_maximum_delay, learning_inputs=inputs, learning_output=output, offset=offset)
        output_estimated = arx_model.simulate(cycle=cycle)
        common.processing.arx.plot_result(output_estimated, output, inputs)
        if correlation:
            common.processing.arx.plot_correlations(output_estimated, output, inputs, maxlags=5)
        if pole_zeros:
            common.processing.arx.plot_zeros_pole(arx_model.get_zeros(), arx_model.get_poles())
        data = list(inputs)
        data.append(output)
        return (output_estimated)


def ARX_model():

        input_labels = ('INDOOR Relative Humidity', 'INDOOR Air Velocity', 'INDOOR_Mean_Radiant_Temp', 'INDOOR_CO2',
                        'Metabolic_Rate (last 15 mins)', 'Clothing_Level')
        input_labels = ('INDOOR Relative Humidity', 'INDOOR_Mean_Radiant_Temp', 'INDOOR Ambient Temp')

        # input_labels = ('total_power_elec_delivered_nt_W_2_REF', 'SetpointBoilerTemperature_REF', 'Tout', 'phi_sun_horizontal', 'phi_sun_north', 'phi_sun_south', 'phi_sun_west', 'phi_sun_east', 'WindSpeed','CurrentHumidity_REF')
        output_label = 'Predicted_Mean_Vote_(PMV)'

        offset = False
        minimum_input_delay = 2
        inputs_maximum_delays = 3
        ouput_maximum_delay = 2

        # training data

        training_starting_stringdatetime = '30/07/2012 01:00:00'
        training_ending_stringdatetime = '31/12/2012 0:00:00'

        # validation data

        validation_starting_stringdatetime = '01/01/2013 0:00:00'
        validation_ending_stringdatetime = '29/07/2013 19:33:26'

        # display

        correlation = False
        pole_zeros = False

        ################################################

        sample_time_in_minutes = 15

        cycle = 5 * 60 / sample_time_in_minutes  # 24 * 60 / sample_time_in_minutes OR None

        print('TRAINING')

        data_container = app.data_container.DataContainer(sample_time_in_secs=sample_time_in_minutes * 60,
                                                                  starting_stringdatetime=training_starting_stringdatetime,
                                                                  ending_stringdatetime=training_ending_stringdatetime)
        print(data_container)
        inputs = [data_container.get_variable_data(data_label) for data_label in input_labels]
        print ("inputs", inputs[1])
        output = data_container.get_variable_data(output_label)
        arx_model = common.processing.arx.Arx(minimum_input_delay=minimum_input_delay,
                                              inputs_maximum_delays=inputs_maximum_delays,
                                              output_maximum_delay=ouput_maximum_delay, learning_inputs=inputs,
                                              learning_output=output, offset=offset)
        output_estimated = arx_model.simulate(cycle=cycle)

        print ("estimated ", output_estimated)
        common.processing.arx.plot_result(output_estimated, output, inputs)
        if correlation:
            common.processing.arx.plot_correlations(output_estimated, output, inputs, maxlags=5)
        if pole_zeros:
            common.processing.arx.plot_zeros_pole(arx_model.get_zeros(), arx_model.get_poles())
        data = list(inputs)
        data.append(output)

        print('VALIDATION')

        data_container = app.data_container.DataContainer(sample_time_in_secs=sample_time_in_minutes * 60, starting_stringdatetime=validation_starting_stringdatetime, ending_stringdatetime=validation_ending_stringdatetime)
        inputs = [data_container.get_variable_data(data_label) for data_label in input_labels]
        output = data_container.get_variable_data(output_label)
        output_estimated = arx_model.simulate(inputs=inputs, output=output, cycle=cycle)
        print('y: %s' % output_label)
        for i in range(len(input_labels)):
            print('u%i: %s' % (i, input_labels[i]))

        data = list(inputs)
        data.append(output)
        common.processing.arx.plot_result(output_estimated, output, inputs)
        print(arx_model)
        common.processing.arx.show()


ARX_model()

# Morris Analysis:
# test = ARX (15,'30/07/2012 01:00:00', '31/12/2012 0:00:00')
# test.model_()