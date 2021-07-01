from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/arithmetic/increment"


def test_zero(flow: FlowTest):

    inputs = {"value": base.Int(0), "increment": base.Int(0)}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Int(0)})


def test_positive(flow: FlowTest):

    inputs = {"value": base.Int(5), "increment": base.Int(1)}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Int(6)})


def test_negative(flow: FlowTest):

    inputs = {"value": base.Int(-5), "increment": base.Int(1)}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Int(-4)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_zero(flow)
        test_positive(flow)
        test_negative(flow)
