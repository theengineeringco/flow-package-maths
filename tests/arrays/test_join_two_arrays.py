import numpy as np
import pytest
from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_py_library_general_maths.array.assemble.join_two_arrays.flow_join_two_arrays import inports, outports
from flow_types import base

# Tests
component_file = "array_maths/assemble/join_two_arrays"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


@pytest.mark.parametrize(
    ("vertical", "result"),
    [
        (True, np.array([[1, 2], [3, 4], [5, 6], [7, 8]])),
        (False, np.array([[1, 2, 5, 6], [3, 4, 7, 8]])),
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
        (True, np.array([[1, 2, 3], [4, 5, 6]])),
        (False, np.array([1, 2, 3, 4, 5, 6])),
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


if __name__ == "__main__":
    with flow_test() as flow:
        # test_equal_arrays(vertical=False, result=np.array([[1, 2, 5, 6], [3, 4, 7, 8]]), flow=flow)
        test_equal_lists(vertical=True, result=np.array([[1, 2, 3], [4, 5, 6]]), flow=flow)
