import numpy as np
import pytest
from flow.test_framework import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.array.sorting.item_by_index.item_by_coord_index.flow_item_by_coord_index import (
    inports,
    outports,
)
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

# Tests
component_file = "array_maths/sorting/item_by_index/item_by_coord_index"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    basic_test_eval(test_data)


@pytest.mark.parametrize(  # noqa: WPS114 - Allow underscore named pattern
    ("index", "result"),
    [
        (base.MdInt(np.array([0, 0])), base.Double(1)),
        (base.MdInt(np.array([1, 3])), base.Double(9)),
        (base.MdInt(np.array([-1, -1])), base.Double(25)),
    ],  # We can test this function multiple times with different values
)
def test_5_2(index: base.MdInt, result: base.Double, flow: FlowTest):
    inputs = {
        inports[0]: base.MdDouble(
            np.array(
                [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
            ),
        ),
        inports[1]: index,
    }

    outputs = {outports[0]: result}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_5_2(index=base.MdInt(np.array([2, 2])), result=base.Double(13), flow=flow)