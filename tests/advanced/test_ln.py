from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/advanced/logarithm/ln"


def test_int(flow: FlowTest):

    val = base.Int(3)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1.0986122886681098)})


def test_log_one(flow: FlowTest):

    val = base.Int(1)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0)})


def test_negative_results(flow: FlowTest):

    val = base.Double(0.222)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(-1.5050778971098575)})


def test_positive_results(flow: FlowTest):

    val = base.Double(1.65)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.5007752879124892)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int(flow)
        test_log_one(flow)
        test_negative_results(flow)
        test_positive_results(flow)
