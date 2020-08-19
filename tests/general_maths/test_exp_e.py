import math

from flow.test_framework import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.general_maths.exp_e.flow_exp_e import inports, outports
from flow.test_framework.helpers import assert_test_data_expected

# Tests
component_file = "general_maths/exp_e"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_exp_e_double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
    }

    outputs = {outports[0]: [base.Double(math.exp(3.67))]}

    run_test_func(inputs, outputs, flow=flow)


def test_exp_e_negatives(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(-10)],
    }

    outputs = {outports[0]: [base.Double(math.exp(-10))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_exp_e_negatives(flow)
