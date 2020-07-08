from pathlib import Path

from flow.testing import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.exp_e.flow_exp_e import exp, inports, outports
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

# Tests


component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    basic_test_eval(test_data)


def test_exp_e_int(flow: FlowTest):
    inputs = {
        inports[0]: [base.Int(10)],
    }

    outputs = {outports[0]: [base.Double(exp(10))]}

    run_test_func(inputs, outputs, flow=flow)


def test_exp_e_double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
    }

    outputs = {outports[0]: [base.Double(exp(3.67))]}

    run_test_func(inputs, outputs, flow=flow)


def test_exp_e_negatives(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(-10)],
    }

    outputs = {outports[0]: [base.Double(exp(-10))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_exp_e_negatives(flow)
