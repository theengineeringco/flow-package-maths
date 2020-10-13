from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_types import base

from flow_package_maths.general_maths.exp_n.flow_exp_n import inports, outports

component_file = "maths/exp_n"


# Tests
def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_exp_n_doubles(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3)],
        inports[1]: [base.Double(-1e2)],
    }

    outputs = {outports[0]: [base.Double(3 ** -1e2)]}

    run_test_func(inputs, outputs, flow=flow)


def test_exp_n_negatives(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(-10)],
        inports[1]: [base.Double(-3)],
    }

    outputs = {outports[0]: [base.Double(-(10 ** -3))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_exp_n_doubles(flow)
