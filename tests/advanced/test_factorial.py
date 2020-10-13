from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/advanced/factorial"


def test_zero_factorial(flow: FlowTest):

    val = base.Int(0)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Int(1)})


def test_small_number(flow: FlowTest):

    val = base.Int(4)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Int(24)})


def test_big_number(flow: FlowTest):

    val = base.Int(12)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Int(479001600)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_zero_factorial(flow)
        test_small_number(flow)
        test_big_number(flow)
