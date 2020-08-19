import numpy as np
from flow.test_framework import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.array.range.flow_range import inports, outports
from flow.test_framework.helpers import assert_test_data_expected

# Tests
component_file = "array_maths/range"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_MdDouble2x2(flow: FlowTest):
    array = base.MdDouble(np.array([[1, 2], [3, 4]]))
    inputs = {inports[0]: [array]}

    outputs = {outports[0]: base.Double(3.0)}

    run_test_func(inputs, outputs, flow=flow)


def test_MdDouble2x2mixed(flow: FlowTest):
    array = base.MdDouble(np.array([[-1, 2.2], [4, 4]]))
    inputs = {inports[0]: [array]}

    outputs = {outports[0]: base.Double(5.0)}

    run_test_func(inputs, outputs, flow=flow)


def test_MdDouble5x5x5x5x5(flow: FlowTest):
    array = base.MdDouble(
        np.array(
            [[1, 1, 1, 1, 1], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
        ),
    )

    inputs = {inports[0]: [array]}

    outputs = {outports[0]: base.Double(24)}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_MdDouble5x5x5x5x5(flow)
