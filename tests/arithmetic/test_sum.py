import numpy as np
from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/arithmetic/sum"


def test_int(flow: FlowTest):

    vals = base.MdDouble(np.linspace(0, 10, 11))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(11 * 10 / 2)})


def test_int_zero_sum(flow: FlowTest):

    vals = base.MdDouble([-3, -2, -1, 0, 1, 2, 3])

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(0)})


def test_decimals(flow: FlowTest):

    test_array = [-1.2e3, 5.432, 0.697, 1, -0.03, 0.0101, 1000.01]
    vals = base.MdDouble(test_array)

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(np.sum(test_array))})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int(flow)
        test_int_zero_sum(flow)
        test_decimals(flow)
