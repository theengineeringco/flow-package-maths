import numpy as np
from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_types import base

from flow_py_library_general_maths.array.assemble.multi_connection_to_int_list.flow_multi_connection_to_int_list import (  # noqa: E501 - allow long line
    inports,
    outports,
)

# Tests
component_file = "array_maths/assemble/multi_connection_to_int_list"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_ints(flow: FlowTest):
    inputs = {inports[0]: [base.Int(1), base.Int(2), base.Int(3), base.Int(5)]}

    array = base.MdInt()
    array.set_array(np.array([1, 2, 3, 5]))
    outputs = {outports[0]: array}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_ints(flow)
