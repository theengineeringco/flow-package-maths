from flow_types import base
from pycomponents_general_maths.util.utils_tests import standard_test
from flow.testing import FlowTest, flow_test
from pathlib import Path

from pycomponents_general_maths.trig_tan.flow_trig_tan import inports, outports
import math


# Tests
component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    global component_file
    test_data = flow.test(component_file, inputs, outputs)
    standard_test(test_data)


def test_tan_double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(0.3)],
    }

    outputs = {outports[0]: [base.Double(math.tan(0.3))]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_tan_double(flow)
