from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_types import base

from flow_py_library_general_maths.general_maths.multiply.flow_multiply import inports, outports

# Tests
component_file = "general_maths/multiply"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


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
