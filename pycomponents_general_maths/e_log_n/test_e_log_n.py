from tec_flow import component
from tec_flow.flow_types import base
from pycomponents_general_maths.util.utils_tests import standard_test

from pycomponents_general_maths.e_log_n.flow_e_log_n import inports, outports
import math


# Tests
def run_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)
    standard_test(test_data)


def test_e_log_n_ints():
    inputs = {
        inports[0]: [base.Int(10)],
        inports[1]: [base.Int(4)],
    }

    outputs = {outports[0]: [base.Double(math.log(10, 4))]}

    run_test_func(inputs, outputs)


def test_e_log_n_double2double():
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(0.4)],
    }

    outputs = {outports[0]: [base.Double(math.log(3.67, 0.4))]}

    run_test_func(inputs, outputs)

if __name__ == "__main__":
    test_e_log_n_ints()