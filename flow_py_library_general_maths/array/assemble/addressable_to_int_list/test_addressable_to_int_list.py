from pathlib import Path

import numpy as np
from flow.testing import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.array.assemble.addressable_to_int_list.flow_addressable_to_int_list import (
    inports,
    outports,
)
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

# Tests

component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    basic_test_eval(test_data)


def test_Ints(flow: FlowTest):
    inputs = {inports[0]: [base.Int(1), base.Int(2), base.Int(3.5), base.Int(5.8),]}

    array = base.MdInt()
    array.set_array(np.array([1, 2, 3.5, 5.8]))
    outputs = {outports[0]: array}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_Ints(flow)
