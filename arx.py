__author__ = 'stephane.ploix@g-scop.grenoble-inp.fr'

import math
import numpy
import numpy.linalg
import matplotlib
import matplotlib.pyplot as plt


class Arx:

    def __init__(self, minimum_input_delay: int, inputs_maximum_delays: list, output_maximum_delay: int, learning_inputs: list, learning_output: list, offset=False):
        """"Estimate ARX coefficients for a dataset.
        :param minimum_input_delay: int standing for the delay_order variable represents the time delay to the system
        :param inputs_maximum_delays: int or list standing for the num_orders variable represents the order for the different inputs
        :param output_maximum_delay: int standing for the den_order variable represents the order for the output
        :param learning_output: list standing for the output variable represents the dataset for output
        :param learning_inputs: list standing for the input variables represent the dataset for input
        :return: the parametric estimated coefficients of inputs and output of the system (numerators, denominator, parametric_estimated_coefficents_for_output, delay_order, den_order, num_orders, output_error, timedelay_for_correlation, output_measured, output_estimated)
        """""

        if type(inputs_maximum_delays) == int:
            num_order = inputs_maximum_delays
            inputs_maximum_delays = [num_order for i in learning_inputs]
        inputs_maximum_delays = [max(0, num_order - minimum_input_delay) for num_order in inputs_maximum_delays]

        self.number_of_parameters = output_maximum_delay + sum(inputs_maximum_delays)
        self.learning_inputs = learning_inputs
        self.learning_output = learning_output
        self.delay = minimum_input_delay
        self.linear_regression_str = 'y[k] = '
        self.numerators = list()
        self.denominator = [1]
        self.parameters = None

        k_init = output_maximum_delay
        for num_order in inputs_maximum_delays:
            k_init = max(k_init, minimum_input_delay + num_order + 1)
        output_measured = list()
        input_measured = list()
        for k in range(k_init, len(learning_output)):
            xrow = list()
            output_measured.append(learning_output[k])
            for i in range(1, output_maximum_delay + 1):
                xrow.append(-learning_output[k - i])
            for i in range(len(learning_inputs)):
                for j in range(0, inputs_maximum_delays[i] + 1):
                    xrow.append(learning_inputs[i][k - minimum_input_delay - j])
            if offset:
                xrow.append(1)
            input_measured.append(xrow)
        input_measured = numpy.matrix(input_measured)
        output_measured = numpy.matrix(output_measured).transpose()

        self.parameters = (numpy.linalg.pinv(input_measured.transpose() * input_measured) * input_measured.transpose() * output_measured).squeeze().tolist()[0]
        parameters_index = 0
        for i in range(0, output_maximum_delay):
            self.denominator.append(self.parameters[parameters_index])
            self.linear_regression_str += ' %+f y[k-%i]' % (-self.parameters[parameters_index], i + 1)
            parameters_index += 1
        self.poles = numpy.roots(self.denominator)

        parameters_index = output_maximum_delay
        self.zeros = list()
        for i in range(len(learning_inputs)):
            numerator = [0 for i in range(self.delay)]
            for j in range(0, inputs_maximum_delays[i] + 1):
                numerator.append(self.parameters[parameters_index])
                if j + self.delay == 0:
                    self.linear_regression_str += ' %+f u%i[k]' % (self.parameters[parameters_index], i)
                else:
                    self.linear_regression_str += ' %+f u%i[k-%i]' % (self.parameters[parameters_index], i, j + self.delay)
                parameters_index += 1
            self.numerators.append(numerator)
            self.zeros.append(numpy.roots(numerator))
        if offset:
            self.offset = self.parameters[-1]
            self.linear_regression_str += ' %+f' % self.offset
        else:
            self.offset = 0

    def get_denominator(self):
        return self.denominator

    def get_numerators(self):
        return self.numerators

    def get_offset(self):
        return self.offset

    def get_delay(self):
        return self.delay

    def get_poles(self):
        return self.poles

    def get_zeros(self):
        return self.zeros

    def simulate(self, inputs=None, output=None, cycle=None):
        if inputs is None:
            inputs = self.learning_inputs
        if output is None:
            output = self.learning_output

        time_shift = len(self.denominator) - 1
        for i in range(len(inputs)):
            time_shift = max(time_shift, len(self.numerators[i]) - 1)
        estimated_output = [output[i] for i in range(time_shift)]
        output_errors = [0 for i in range(time_shift)]
        denominator_impact = [0 for x in self.denominator]
        numerators_impact = list()
        for numerator in self.numerators:
            numerators_impact.append([0 for x in numerator])
        for k in range(time_shift, len(output)):
            y_k = self.offset
            for i in range(1, len(self.denominator)):
                if cycle is not None and k >= cycle and (k % cycle) == 0:
                    delta = -self.denominator[i] * output[k - i]
                else:
                    delta = -self.denominator[i] * estimated_output[k - i]
                y_k += delta
                denominator_impact[i] += abs(delta)
            for i in range(len(self.numerators)):
                for j in range(0, len(self.numerators[i])):
                    delta = self.numerators[i][j] * inputs[i][k - j]
                    y_k += delta
                    numerators_impact[i][j] += abs(delta)
            denominator_impact[0] += abs(y_k)
            estimated_output.append(y_k)
            output_errors.append(y_k - output[k])
        normalization_impact = sum(denominator_impact[1:])
        for numerator_impact in numerators_impact:
            normalization_impact += sum(numerator_impact)
        for i in range(len(denominator_impact)):
            denominator_impact[i] = denominator_impact[i] / normalization_impact
        for i in range(len(numerators_impact)):
            for j in range(len(numerators_impact[i])):
                numerators_impact[i][j] = numerators_impact[i][j] / normalization_impact
        for i in range(1, len(self.denominator)):
            print('impact y[k-%i] = %f%% ' % (i, 100 * denominator_impact[i]))
        for i in range(len(self.numerators)):
            for j in range(0, len(self.numerators[i])):
                if j == 0:
                    print('impact u%i[k] = %f%% ' % (i, 100 * numerators_impact[i][j]))
                else:
                    print('impact u%i[k-%i] = %f%% ' % (i, j, 100 * numerators_impact[i][j]))
        loss_function = (sum([error ** 2 for error in output_errors]) / len(output_errors)) / 2
        akaike_value = (1 + self.number_of_parameters / len(output_errors)) / (1 - self.number_of_parameters / len(output_errors)) * loss_function
        print('Average output error = %f' % (sum(output_errors) / len(output_errors)))
        print('Average absolute output error = %f' % (sum([abs(error) for error in output_errors]) / len(output_errors)))
        print('AKAIKE value = %f' % akaike_value)
        print('Max output error = %f' % max(output_errors))
        print('Min output error = %f' % min(output_errors))
        print('Standard deviation for output error = %f' % numpy.std(output_errors))
        return estimated_output

    def __str__(self):
        string = 'linear regression: ' + self.linear_regression_str + '\n'
        return string


def plot_zeros_pole(zeros: 'list of lists', poles: list):
    if type(zeros[0]) == int:
        number_of_plots = 1
    else:
        number_of_plots = len(zeros)
    number_of_rows = math.floor(math.sqrt(number_of_plots))
    number_of_columns = math.ceil(number_of_plots / number_of_rows)
    fig = plt.figure()
    fig.suptitle('zeros-poles analysis')
    for i in range(0, len(zeros)):
        axes = fig.add_subplot(number_of_rows, number_of_columns, i + 1)
        axes.set_xlabel('input' + str(i))
        # create the unit circle
        create_unit_circle = matplotlib.patches.Circle((0, 0), radius=1, fill=False, color='black', ls='dashed')
        axes.add_patch(create_unit_circle)
        # Plot the zeros and set marker properties
        plot_zeros = axes.plot(zeros[i].real, zeros[i].imag, 'go', ms=10)
        plt.setp(plot_zeros, markersize=10.0, markeredgewidth=1.0, markeredgecolor='k', markerfacecolor='g')
        # Plot the poles and set marker properties
        plot_poles = axes.plot(poles.real, poles.imag, 'rx', ms=10)
        plt.setp(plot_poles, markersize=12.0, markeredgewidth=3.0, markeredgecolor='r', markerfacecolor='r')
        axes.spines['left'].set_position('center')
        axes.spines['bottom'].set_position('center')
        axes.spines['right'].set_visible(False)
        axes.spines['top'].set_visible(False)
        # set the ticks
        radius = 1.5
        axes.axis('scaled')
        axes.axis([-radius, radius, -radius, radius])
        ticks = [-1, -.5, .5, 1]
        plt.xticks(ticks)
        plt.yticks(ticks)
        axes.grid()
    fig.tight_layout()


def plot_result(output_estimated: list, output_measured: list, inputs_measured: 'list  of lists'=None):
    output_errors = [output_measured[k] - output_estimated[k] for k in range(len(output_measured))]
    fig, axes = plt.subplots(nrows=2, ncols=1)
    axes[0].plot(output_measured)
    axes[0].plot(output_estimated)
    axes[0].grid()
    axes[0].legend(('measured', 'estimated'), loc=0)
    axes[0].set_xlim(left=0, right=len(output_estimated))
    axes[1].plot(output_errors)
    axes[1].grid()
    axes[1].legend(('error',), loc=0)
    axes[1].set_xlim(left=0, right=len(output_errors))
    fig.tight_layout()


def plot_correlations(output_estimated: list, output_measured: list, inputs_measured: 'list  of lists'=None, maxlags: int=5):
    output_errors = [output_measured[k] - output_estimated[k] for k in range(len(output_measured))]
    fig, axes = plt.subplots()  # auto-correlation
    fig.suptitle("Auto-correlation")
    axes.acorr(output_errors, normed=True, usevlines=True, maxlags=maxlags)
    axes.set_xlim([-maxlags - 0.5, maxlags + 0.5])
    plt.tight_layout()

    if inputs_measured is not None:  # cross-correlation
        number_of_plots = len(inputs_measured)
        number_of_rows = math.ceil(math.sqrt(number_of_plots))
        number_of_columns = math.ceil(math.sqrt(number_of_plots))
        fig = plt.figure()
        fig.suptitle('cross correlation analysis')
        for i in range(0, len(inputs_measured)):
            axes = fig.add_subplot(number_of_rows, number_of_columns, i + 1)
            axes.set_xlabel('input' + str(i))
            axes.xcorr(output_errors, inputs_measured[i], normed=True, usevlines=True, maxlags=maxlags)
            axes.set_xlim([-maxlags - 0.5, 0.5])
            axes.grid()
        fig.tight_layout()

    average_error = (sum(output_errors) / len(output_errors))
    average_absolute_error = (sum([abs(error) for error in output_errors]) / len(output_errors))
    mse = (sum([ (error*error) for error in output_errors]) / len(output_errors))
    max_error = max(output_errors)
    min_error = min(output_errors)
    std_error = numpy.std(output_errors)
    return average_error, average_absolute_error, max_error, min_error, std_error


def mse (output_estimated: list, output_measured: list):
    output_errors = [output_measured[k] - output_estimated[k] for k in range(len(output_measured))]
    mse2 = (sum([(error**2) for error in output_errors]) / len(output_errors))
    return mse2


def show():
    plt.show()
