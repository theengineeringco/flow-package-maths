from pathlib import Path

import numpy as np
from flow.testing import FlowTest, flow_test
from flow_types import base

from pycomponents_general_maths.array.assemble.join_two_arrays.flow_join_two_arrays import inports, outports
from pycomponents_general_maths.util.utils_tests import basic_test_eval

# Tests

component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs, timeout=1000)
    basic_test_eval(test_data)


def test_equal_arrays_vertical(flow: FlowTest):
    inputs = {
        inports[0]: [base.MdDouble(np.array([[1, 2], [3, 4]]))],
        inports[1]: [base.MdDouble(np.array([[5, 6], [7, 8]]))],
    }

    outputs = {outports[0]: base.MdDouble(np.array([[1, 2], [3, 4], [5, 6], [7, 8]]))}

    run_test_func(inputs, outputs, flow=flow)


def test_equal_arrays_horizontal(flow: FlowTest):
    inputs = {
        inports[0]: [base.MdDouble(np.array([[1, 2], [3, 4]]))],
        inports[1]: [base.MdDouble(np.array([[5, 6], [7, 8]]))],
        "vertical": base.Bool(False),
    }

    outputs = {outports[0]: base.MdDouble(np.array([[1, 2, 5, 6], [3, 4, 7, 8]]))}

    run_test_func(inputs, outputs, flow=flow)


def test_unequal_arrays(flow: FlowTest):
    try:
        inputs = {
            inports[0]: [base.MdDouble(np.array([1, 2, 3, 4]))],
            inports[1]: [base.MdDouble(np.array([[5, 6], [7, 8]]))],
            "vertical": base.Bool(False),
        }

        outputs = {outports[0]: base.MdDouble(np.array([[1, 2, 5, 6], [3, 4, 7, 8]]))}

        run_test_func(inputs, outputs, flow=flow)
    except ValueError:
        print("This is not allowed, the arrays are the wrong shape!")


if __name__ == "__main__":
    with flow_test() as flow:
        test_equal_arrays_vertical(flow)
        # test_equal_arrays_horizontal(flow)
        # test_unequal_arrays(flow)
