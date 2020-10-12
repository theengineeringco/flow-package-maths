import numpy as np
from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_py_library_general_maths.array.assemble.make_number_collection.flow_make_number_collection import (  # noqa: E501
    inports,
    outports,
)
from flow_types import base

# Tests
component_file = "array_maths/assemble/make_number_collection"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_doubles(flow: FlowTest):
    inputs = {inports[0]: [base.Double(1), base.Double(2), base.Double(3.5), base.Double(5.8)]}

    array = base.MdDouble()
    array.set_array(np.array([1, 2, 3.5, 5.8]))
    outputs = {outports[0]: array}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_doubles(flow)
