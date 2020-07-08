from pathlib import Path

import numpy as np
import pytest
from flow.testing import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.array.assemble.join_two_arrays.flow_join_two_arrays import inports, outports
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

# Tests

component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs, timeout=1000)
    basic_test_eval(test_data)


@pytest.mark.parametrize(
    ("vertical", "result"),
    [
        (False, np.array([[1, 2, 5, 6], [3, 4, 7, 8]])),
        (True, np.array([[1, 2], [3, 4], [5, 6], [7, 8]])),
    ],  # We can test this function multiple times with different values
)
def test_equal_arrays(vertical, result, flow: FlowTest):
    inputs = {
        inports[0]: [base.MdDouble(np.array([[1, 2], [3, 4]]))],
        inports[1]: [base.MdDouble(np.array([[5, 6], [7, 8]]))],
        "vertical": base.Bool(vertical),
    }
    outputs = {outports[0]: base.MdDouble(result)}
    run_test_func(inputs, outputs, flow=flow)


@pytest.mark.parametrize(
    ("vertical", "result"),
    [
        (False, np.array([[1, 2, 3], [4, 5, 6]])),
        (True, np.array([1, 2, 3, 4, 5, 6])),
    ],  # We can test this function multiple times with different values
)
def test_equal_lists(vertical, result, flow: FlowTest):
    inputs = {
        inports[0]: [base.MdDouble(np.array([1, 2, 3]))],
        inports[1]: [base.MdDouble(np.array([4, 5, 6]))],
        "vertical": base.Bool(vertical),
    }
    outputs = {outports[0]: base.MdDouble(result)}
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
        # test_equal_arrays(False, np.array([[1, 2, 5, 6], [3, 4, 7, 8]]), flow)
        test_equal_lists(True, np.array([[1, 2, 3], [4, 5, 6]]), flow)
        # test_unequal_arrays(flow)
