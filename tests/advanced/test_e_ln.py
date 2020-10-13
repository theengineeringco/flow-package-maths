import math

from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_types import base

from flow_package_maths.general_maths.e_ln.flow_e_ln import inports, outports

# Tests
component_file = "maths/e_ln"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_ln_double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
    }

    outputs = {outports[0]: [base.Double(math.log(3.67))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_ln_double(flow)
