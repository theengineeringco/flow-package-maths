from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/arithmetic/divide"


def test_int(flow: FlowTest):

    num = base.Int(10)
    denom = base.Int(5)

    inputs = {"numerator": num, "denominator": denom}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(2)})


def test_int2double(flow: FlowTest):

    num = base.Int(5)
    denom = base.Int(2)

    inputs = {"numerator": num, "denominator": denom}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(2.5)})


def test_negative_int(flow: FlowTest):

    num = base.Int(-4)
    denom = base.Int(-2)

    inputs = {"numerator": num, "denominator": denom}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(2)})


def test_decimals(flow: FlowTest):

    num = base.Double(0.99)
    denom = base.Double(0.99)

    inputs = {"numerator": num, "denominator": denom}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1)})


def test_negative_doubles(flow: FlowTest):

    num = base.Double(-1.2e6)
    denom = base.Double(2.5)

    inputs = {"numerator": num, "denominator": denom}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(-480000)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int(flow)
        test_int2double(flow)
        test_negative_int(flow)
        test_decimals(flow)
        test_negative_doubles(flow)
