from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_types import base

from flow_py_library_general_maths.general_maths.divide.flow_divide import inports, outports

# Tests
component_file = "maths/divide"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_divide_double2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(-1e9)],
    }

    outputs = {outports[0]: [base.Double(3.67 / (-1e9))]}

    run_test_func(inputs, outputs, flow=flow)


def test_divide_int2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Int(1000)],
        inports[1]: [base.Int(255)],
    }

    outputs = {outports[0]: [base.Double(3.9215686274509802)]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_divide_double2double(flow)
        test_divide_int2double(flow)
