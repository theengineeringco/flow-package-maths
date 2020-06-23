from pathlib import Path

from flow.testing import FlowTest, flow_test
from flow_types import base

from pycomponents_general_maths.array.sum.flow_sum import inports, outports
from pycomponents_general_maths.util.utils_tests import standard_test
import numpy as np

# Tests

component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    global component_file
    test_data = flow.test(component_file, inputs, outputs)
    standard_test(test_data)


def test_MdDouble2x2(flow: FlowTest):
    array = base.MdDouble()
    array.from_np(np.array([[1, 2], [3, 4]]))

    inputs = {inports[0]: [array]}

    outputs = {outports[0]: base.Double(10)}

    run_test_func(inputs, outputs, flow=flow)


def test_MdDouble5x5x5x5x5(flow: FlowTest):
    array = base.MdDouble()
    array.from_np(
        np.array(
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25],],
        )
    )

    inputs = {inports[0]: [array]}

    outputs = {outports[0]: base.Double(325)}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_MdDouble5x5x5x5x5(flow)
