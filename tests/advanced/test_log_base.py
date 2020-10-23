import math

from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/advanced/logarithm/log_base"


def test_int2int(flow: FlowTest):

    val = base.Int(8)
    log_base = base.Int(2)

    inputs = {"value": val, "base": log_base}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(3)})


def test_int2double(flow: FlowTest):

    val = base.Int(3)
    log_base = base.Int(2)

    inputs = {"value": val, "base": log_base}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(math.log(3, 2))})


def test_doubles(flow: FlowTest):

    val = base.Double(1.26)
    log_base = base.Double(0.396)

    inputs = {"value": val, "base": log_base}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(math.log(1.26, 0.396))})


if __name__ == "__main__":
    with flow_test() as flow:
        test_int2int(flow)
        test_int2double(flow)
        test_doubles(flow)
