from pathlib import Path

from flow.testing import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.exp_n.flow_exp_n import inports, outports
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

component_file = Path(__file__).parent


# Tests
def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    basic_test_eval(test_data)


def test_exp_n_ints(flow: FlowTest):
    inputs = {
        inports[0]: [base.Int(10)],
        inports[1]: [base.Int(4)],
    }

    outputs = {outports[0]: [base.Double(10 ** 4)]}

    run_test_func(inputs, outputs, flow=flow)


def test_exp_n_doubles(flow: FlowTest):
    inputs = {
        inports[0]: [base.Int(3)],
        inports[1]: [base.Double(-1e2)],
    }

    outputs = {outports[0]: [base.Double(3 ** -1e2)]}

    run_test_func(inputs, outputs, flow=flow)


def test_exp_n_negatives(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(-10)],
        inports[1]: [base.Double(-3)],
    }

    outputs = {outports[0]: [base.Double((((-(10 ** -3)))))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_exp_n_doubles(flow)
