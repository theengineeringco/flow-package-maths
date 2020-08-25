import math

from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_types import base, eng

from flow_py_library_general_maths.general_maths.trig_cos.flow_trig_cos import inports, outports

# Tests
component_file = "maths/trig_cos"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_cos_double(flow: FlowTest):
    inputs = {
        inports[0]: [eng.Angle(0.3)],
    }

    outputs = {outports[0]: [base.Double(math.cos(0.3))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_cos_double(flow)