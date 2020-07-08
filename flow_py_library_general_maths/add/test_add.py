from pathlib import Path

from flow.testing import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.add.flow_add import inports, outports
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

# Tests
component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    basic_test_eval(test_data)


def test_add_ints(flow: FlowTest):
    inputs = {
        inports[0]: [base.Int(1)],
        inports[1]: [base.Int(4)],
    }

    outputs = {outports[0]: [base.Double(5)]}

    run_test_func(inputs, outputs, flow)


def test_add_int2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Int(2)],
    }

    outputs = {outports[0]: [base.Double(5.67)]}

    run_test_func(inputs, outputs, flow)


def test_add_double2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(-1e9)],
    }

    outputs = {outports[0]: [base.Double((-1e9) + 3.67)]}

    run_test_func(inputs, outputs, flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_add_ints(flow)
