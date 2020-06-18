from flow_types import base
from pycomponents_general_maths.util.utils_tests import standard_test
from flow.testing import FlowTest, flow_test
from pathlib import Path

from pycomponents_general_maths.multiply.flow_multiply import inports, outports


# Tests
component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    global component_file
    test_data = flow.test(component_file, inputs, outputs)
    standard_test(test_data)


def test_multiply_ints(flow: FlowTest):
    inputs = {
        inports[0]: [base.Int(1)],
        inports[1]: [base.Int(4)],
    }

    outputs = {outports[0]: [base.Double(4)]}

    run_test_func(inputs, outputs, flow=flow)


def test_multiply_int2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Int(2)],
    }

    outputs = {outports[0]: [base.Double(3.67 * 2)]}

    run_test_func(inputs, outputs, flow=flow)


def test_multiply_double2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(-1e9)],
    }

    outputs = {outports[0]: [base.Double(3.67 * (-1e9))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_multiply_double2double(flow)
