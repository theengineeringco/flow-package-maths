import math

from flow.test_framework import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.general_maths.e_ln.flow_e_ln import inports, outports
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

# Tests
component_file = "general_maths/e_ln"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    basic_test_eval(test_data)


def test_ln_double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
    }

    outputs = {outports[0]: [base.Double(math.log(3.67))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_ln_double(flow)