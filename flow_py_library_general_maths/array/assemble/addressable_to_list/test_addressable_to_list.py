import numpy as np
from flow.test_framework import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.array.assemble.addressable_to_list.flow_addressable_to_list import inports, outports
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

# Tests
component_file = "general_maths/array/assemble/addressable_to_list"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    basic_test_eval(test_data)


def test_doubles(flow: FlowTest):
    inputs = {inports[0]: [base.Double(1), base.Double(2), base.Double(3.5), base.Double(5.8)]}

    array = base.MdDouble()
    array.set_array(np.array([1, 2, 3.5, 5.8]))
    outputs = {outports[0]: array}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_doubles(flow)
