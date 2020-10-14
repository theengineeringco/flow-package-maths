import numpy as np
from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/statistics/range"


def test_unsorted_int_list(flow: FlowTest):

    vals = base.MdDouble(np.array([3, 1, 6, 9, 13, 2]))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(12)})


def test_int_zero(flow: FlowTest):

    vals = base.MdDouble(np.array([2, 2, 2, 2]))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(0)})


def test_doubles(flow: FlowTest):

    vals = base.MdDouble(np.array([-1.2e3, 5.432, 0.697, 1, -0.03, 0.0101, 1000.01]))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(2200.01)})


def test_matrix(flow: FlowTest):

    test_array = [[1.1, 1.2], [1.3, 1.4]]
    vals = base.MdDouble(np.array(test_array))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(np.ptp(test_array))})


def test_d4_array(flow: FlowTest):

    test_array = [
        [
            [[12.5, -2], [12.5, -2]],
            [[12.5, -2], [12.5, -2]],
            [[12.5, -2], [12.5, -2]],
            [[12.5, -2], [12.5, -2]],
        ],
    ]
    vals = base.MdDouble(np.array(test_array))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(np.ptp(test_array))})


if __name__ == "__main__":
    with flow_test() as flow:
        test_unsorted_int_list(flow)
        test_int_zero(flow)
        test_doubles(flow)
        test_matrix(flow)
        test_d4_array(flow)
