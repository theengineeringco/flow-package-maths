from tec_flow import component
from tec_flow.flow_types import base
from pycomponents_general_maths.util.utils_tests import standard_test

from pycomponents_general_maths.exp_e.flow_exp_e import inports, outports, exp

# Tests


def run_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)
    standard_test(test_data)


def test_exp_e_int():
    inputs = {
        inports[0]: [base.Int(10)],
    }

    outputs = {outports[0]: [base.Double(exp(10))]}

    run_test_func(inputs, outputs)


def test_exp_e_double():
    inputs = {
        inports[0]: [base.Double(3.67)],
    }

    outputs = {outports[0]: [base.Double(exp(3.67))]}

    run_test_func(inputs, outputs)


def test_exp_e_negatives():
    inputs = {
        inports[0]: [base.Double(-10)],
    }

    outputs = {outports[0]: [base.Double(exp(-10))]}

    run_test_func(inputs, outputs)
