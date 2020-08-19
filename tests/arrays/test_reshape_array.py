import numpy as np
from flow.test_framework import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.array.assemble.reshape_array.flow_reshape_array import inports, outports
from flow.test_framework.helpers import assert_test_data_expected

# Tests
component_file = "array_maths/assemble/reshape_array"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs, 1200)
    assert_test_data_expected(test_data)


def test_5_2_to_3_3_3(flow: FlowTest):  # noqa: WPS114 - Allow underscore named pattern
    inputs = {
        inports[0]: base.MdDouble(
            np.array(
                [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
            ),
        ),
        inports[1]: base.MdInt(np.array([3, 3, 3])),
    }

    outputs = {
        outports[0]: base.MdDouble(
            np.array(
                [
                    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                    [[19, 20, 21], [22, 23, 24], [25, 0, 0]],
                ],
            ),
        ),
    }

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_5_2_to_3_3_3(flow)
