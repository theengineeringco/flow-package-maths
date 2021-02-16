import numpy as np
from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir_max = "flow_package_maths/advanced/max"
component_dir_min = "flow_package_maths/advanced/min"


def test_single_element(flow: FlowTest):

    test_array = [1]
    vals = base.MdDouble(test_array)

    inputs = {"values": vals}
    outputs = ["result"]
    test_data_max = flow.test(component_dir_max, inputs, outputs)
    test_data_min = flow.test(component_dir_min, inputs, outputs)
    assert check_outport_data(test_data_max, {"result": base.Double(1)})
    assert check_outport_data(test_data_min, {"result": base.Double(1)})


def test_list_input(flow: FlowTest):

    test_array = [0.1, 1, 3, -4, 9.2553, 0.0422]
    vals = base.MdDouble(test_array)

    inputs = {"values": vals}
    outputs = ["result"]
    test_data_max = flow.test(component_dir_max, inputs, outputs)
    test_data_min = flow.test(component_dir_min, inputs, outputs)
    assert check_outport_data(test_data_max, {"result": base.Double(np.max(test_array))})
    assert check_outport_data(test_data_min, {"result": base.Double(np.min(test_array))})


def test_repeated_values(flow: FlowTest):

    test_array = [100.2, 0.1, 1, 3, -4, 0, 100.2, -4, 0.1, 1, 6.42]
    vals = base.MdDouble(test_array)

    inputs = {"values": vals}
    outputs = ["result"]
    test_data_max = flow.test(component_dir_max, inputs, outputs)
    test_data_min = flow.test(component_dir_min, inputs, outputs)
    assert check_outport_data(test_data_max, {"result": base.Double(np.max(test_array))})
    assert check_outport_data(test_data_min, {"result": base.Double(np.min(test_array))})


if __name__ == "__main__":
    with flow_test() as flow:
        test_single_element(flow)
        test_list_input(flow)
        test_repeated_values(flow)
