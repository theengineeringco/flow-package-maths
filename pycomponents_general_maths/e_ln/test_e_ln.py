from tec_flow import component
from tec_flow.flow_types import base
from pycomponents_general_maths.util.utils_tests import standard_test

from pycomponents_general_maths.e_ln.flow_e_ln import inports, outports
import math

# Tests


def run_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)
    standard_test(test_data)


def test_ln_int():
    inputs = {
        inports[0]: [base.Int(10)],
    }

    outputs = {outports[0]: [base.Double(math.log(10))]}

    run_test_func(inputs, outputs)


def test_ln_double():
    inputs = {
        inports[0]: [base.Double(3.67)],
    }

    outputs = {outports[0]: [base.Double(math.log(3.67))]}

    run_test_func(inputs, outputs)
