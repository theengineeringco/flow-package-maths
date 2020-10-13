import math

from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir_acos = "flow_package_maths/advanced/trigonometry/acos"
component_dir_asin = "flow_package_maths/advanced/trigonometry/asin"
component_dir_atan = "flow_package_maths/advanced/trigonometry/atan"
component_dir_cos = "flow_package_maths/advanced/trigonometry/cos"
component_dir_sin = "flow_package_maths/advanced/trigonometry/sin"
component_dir_tan = "flow_package_maths/advanced/trigonometry/tan"


def test_acos_int(flow: FlowTest):

    val = base.Int(1)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir_acos, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0)})


def test_acos_double(flow: FlowTest):

    val = base.Double(0.52)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir_acos, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1.0239453760989525)})


def test_asin_int(flow: FlowTest):

    val = base.Int(1)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir_asin, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(math.pi / 2)})


def test_asin_double(flow: FlowTest):

    val = base.Double(0.52)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir_asin, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.5468509506959441)})


def test_atan_int(flow: FlowTest):

    val = base.Int(3)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir_atan, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1.2490457723982544)})


def test_atan_double(flow: FlowTest):

    val = base.Double(0.52)

    inputs = {"value": val}
    outputs = ["result"]
    test_data = flow.test(component_dir_atan, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.4795192919925962)})


def test_cos_int(flow: FlowTest):

    angle = base.Int(0)

    inputs = {"angle": angle}
    outputs = ["result"]
    test_data = flow.test(component_dir_cos, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1)})


def test_cos_double(flow: FlowTest):

    angle = base.Double(math.pi)

    inputs = {"angle": angle}
    outputs = ["result"]
    test_data = flow.test(component_dir_cos, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(-1)})


def test_sin_int(flow: FlowTest):

    angle = base.Int(1)

    inputs = {"angle": angle}
    outputs = ["result"]
    test_data = flow.test(component_dir_sin, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.8414709848078965)})


def test_sin_double(flow: FlowTest):

    angle = base.Double(math.pi / 2)

    inputs = {"angle": angle}
    outputs = ["result"]
    test_data = flow.test(component_dir_sin, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1)})


def test_tan_int(flow: FlowTest):

    angle = base.Int(1)

    inputs = {"angle": angle}
    outputs = ["result"]
    test_data = flow.test(component_dir_tan, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(1.5574077246549023)})


def test_tan_double(flow: FlowTest):

    angle = base.Double(0.52)

    inputs = {"angle": angle}
    outputs = ["result"]
    test_data = flow.test(component_dir_tan, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Double(0.5725618302516684)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_acos_int(flow)
        test_acos_double(flow)
        test_asin_int(flow)
        test_asin_double(flow)
        test_atan_int(flow)
        test_atan_double(flow)
        test_cos_int(flow)
        test_cos_double(flow)
        test_sin_int(flow)
        test_sin_double(flow)
        test_tan_int(flow)
        test_tan_double(flow)
