from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/advanced/power"


def test_int(flow: FlowTest):

    val = base.Int(8)
    exponent = base.Int(2)

    inputs = {"value": val, "exponent": exponent}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(64)})


def test_negative_int_exponent(flow: FlowTest):

    val = base.Int(8)
    exponent = base.Int(-3)

    inputs = {"value": val, "exponent": exponent}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(8 ** -3)})


def test_decimal_exponent(flow: FlowTest):

    val = base.Int(4)
    exponent = base.Double(0.5)

    inputs = {"value": val, "exponent": exponent}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(2)})


def test_doubles(flow: FlowTest):

    val = base.Double(0.431)
    exponent = base.Double(1.984)

    inputs = {"value": val, "exponent": exponent}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.431 ** 1.984)})


def test_doubles_negative_exponent(flow: FlowTest):

    val = base.Double(0.431)
    exponent = base.Double(-1.984)

    inputs = {"value": val, "exponent": exponent}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.431 ** -1.984)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int(flow)
        test_negative_int_exponent(flow)
        test_decimal_exponent(flow)
        test_doubles(flow)
        test_doubles_negative_exponent(flow)
