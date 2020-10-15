from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/arithmetic/absolute"


def test_int(flow: FlowTest):

    val = base.Int(3)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(3)})


def test_negative_int(flow: FlowTest):

    val = base.Int(-3)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(3)})


def test_decimal(flow: FlowTest):

    val = base.Double(0.99)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.99)})


def test_negative_decimal(flow: FlowTest):

    val = base.Double(-0.99)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.99)})


def test_double(flow: FlowTest):

    val = base.Double(1.3101e6)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1.3101e6)})


def test_negative_double(flow: FlowTest):

    val = base.Double(-1.3101e6)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1.3101e6)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int(flow)
        test_negative_int(flow)
        test_decimal(flow)
        test_negative_decimal(flow)
        test_double(flow)
        test_negative_double(flow)
