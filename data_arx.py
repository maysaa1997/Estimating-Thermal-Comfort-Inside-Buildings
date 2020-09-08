__author__ = 'maysaa.khalil@utt.fr'

import app.data_container
import common.processing.arx
from datetime import datetime
startTime = datetime.now()
# model configuration


input_labels = (
    'INDOOR Relative Humidity',  'INDOOR Air Velocity',
    'INDOOR Ambient Temp',
    'Metabolic_Rate (last 15 mins)')

output_label = 'Predicted_Mean_Vote_(PMV)'

offset = False
minimum_input_delay = 0
inputs_maximum_delays = 0
ouput_maximum_delay = 1

# training data

training_starting_stringdatetime = '30/07/2012 01:00:00'
# training_ending_stringdatetime = '31/12/2012 0:00:00'
training_ending_stringdatetime = '31/05/2013 0:00:00'

# validation data

#validation_starting_stringdatetime = '01/01/2013 0:00:00'
validation_starting_stringdatetime = '01/06/2013 0:00:00'
#validation_ending_stringdatetime = '29/07/2013 19:33:26'
validation_ending_stringdatetime = '31/07/2013 19:00:00'

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
output = data_container.get_variable_data(output_label)
arx_model = common.processing.arx.Arx(minimum_input_delay=minimum_input_delay,
                                      inputs_maximum_delays=inputs_maximum_delays,
                                      output_maximum_delay=ouput_maximum_delay, learning_inputs=inputs,
                                      learning_output=output, offset=offset)
output_estimated = arx_model.simulate(cycle=cycle)
common.processing.arx.plot_result(output_estimated, output, inputs)
if correlation:
    common.processing.arx.plot_correlations(output_estimated, output, inputs, maxlags=5)
if pole_zeros:
    common.processing.arx.plot_zeros_pole(arx_model.get_zeros(), arx_model.get_poles())
data = list(inputs)
data.append(output)

print(datetime.now() - startTime)

print('VALIDATION')

data_container = app.data_container.DataContainer(sample_time_in_secs=sample_time_in_minutes * 60,
                                                  starting_stringdatetime=training_ending_stringdatetime,
                                                  ending_stringdatetime=validation_ending_stringdatetime)
inputs = [data_container.get_variable_data(data_label) for data_label in input_labels]
output = data_container.get_variable_data(output_label)
output_estimated = arx_model.simulate(inputs=inputs, output=output, cycle=cycle)
print('y: %s' % output_label)
for i in range(len(input_labels)):
    print('u%i: %s' % (i, input_labels[i]))


print(datetime.now() - startTime)
data = list(inputs)
data.append(output)
common.processing.arx.plot_result(output_estimated, output, inputs)
print(arx_model)
common.processing.arx.show()

mse = common.processing.arx.mse(output_estimated, output)

print(mse)