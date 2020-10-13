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

    vals = base.MdDouble(np.array([-3, -2, -1, 0, 1, 2, 3]))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(0)})


def test_decimals(flow: FlowTest):

    vals = base.MdDouble(np.array([-1.2e3, 5.432, 0.697, 1, -0.03, 0.0101, 1000.01]))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(-192.8809000000001)})


def test_matrix(flow: FlowTest):

    vals = base.MdDouble(np.array([[1.1, 1.2], [1.3, 1.4]]))

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(5)})


def test_4d_array(flow: FlowTest):

    vals = base.MdDouble(
        np.array(
            [
                [
                    [[1.1, 2], [1.1, 2]],
                    [[1.1, 2], [1.1, 2]],
                    [[1.1, 2], [1.1, 2]],
                    [[1.1, 2], [1.1, 2]],
                ],
            ],
        ),
    )

    inputs = {"values": vals}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)

    # using sum of arithmetic series formula for test
    assert check_outport_data(test_data, {"result": base.Double(24.8)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int(flow)
        test_int_zero_sum(flow)
        test_decimals(flow)
        test_matrix(flow)
        test_4d_array(flow)
