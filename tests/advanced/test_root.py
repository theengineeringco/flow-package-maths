from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/advanced/root"


def test_int(flow: FlowTest):

    val = base.Int(4)
    root = base.Int(2)

    inputs = {"value": val, "root": root}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(2)})


def test_negative_int_root(flow: FlowTest):

    val = base.Int(4)
    root = base.Int(-2)

    inputs = {"value": val, "root": root}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.5)})


def test_decimal_root(flow: FlowTest):

    val = base.Int(4)
    exponent = base.Double(0.5)

    inputs = {"value": val, "root": exponent}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(16)})


def test_doubles(flow: FlowTest):

    val = base.Double(0.431)
    exponent = base.Double(1.984)

    inputs = {"value": val, "root": exponent}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.6542816693895579)})


def test_doubles_negative_root(flow: FlowTest):

    val = base.Double(0.431)
    exponent = base.Double(-1.984)

    inputs = {"value": val, "root": exponent}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1.5283937282439777)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int(flow)
        test_negative_int_root(flow)
        test_decimal_root(flow)
        test_doubles(flow)
        test_doubles_negative_root(flow)
