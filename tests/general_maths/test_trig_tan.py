import math

from flow.test_framework import FlowTest, flow_test
from flow_types import base, eng

from flow_py_library_general_maths.general_maths.trig_tan.flow_trig_tan import inports, outports
from flow.test_framework.helpers import assert_test_data_expected

# Tests
component_file = "general_maths/trig_tan"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_tan_double(flow: FlowTest):
    inputs = {
        inports[0]: [eng.Angle(0.3)],
    }

    outputs = {outports[0]: [base.Double(math.tan(0.3))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_tan_double(flow)
