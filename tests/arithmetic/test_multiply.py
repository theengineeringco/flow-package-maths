from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/arithmetic/multiply"


def test_int(flow: FlowTest):

    val1 = base.Int(10)
    val2 = base.Int(5)

    inputs = {"value1": val1, "value2": val2}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(50)})


def test_negative_int(flow: FlowTest):

    val1 = base.Int(-4)
    val2 = base.Int(-2)

    inputs = {"value1": val1, "value2": val2}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(8)})


def test_decimals(flow: FlowTest):

    val1 = base.Double(0.99)
    val2 = base.Double(0.99)

    inputs = {"value1": val1, "value2": val2}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.9801)})


def test_negative_doubles(flow: FlowTest):

    val1 = base.Double(-1.2e6)
    val2 = base.Double(2.5)

    inputs = {"value1": val1, "value2": val2}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(-3000000)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int(flow)
        test_negative_int(flow)
        test_decimals(flow)
        test_negative_doubles(flow)
