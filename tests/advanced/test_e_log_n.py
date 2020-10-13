import math

from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_types import base

from flow_package_maths.general_maths.e_log_n.flow_e_log_n import inports, outports

component_file = "maths/e_log_n"


# Tests
def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_e_log_n_double2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(0.4)],
    }

    outputs = {outports[0]: [base.Double(math.log(3.67, 0.4))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_e_log_n_double2double(flow)
