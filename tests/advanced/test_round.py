from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir_nearest = "flow_package_maths/advanced/round/round_nearest"
component_dir_up = "flow_package_maths/advanced/round/round_up"
component_dir_down = "flow_package_maths/advanced/round/round_down"


def test_round_integer(flow: FlowTest):

    val = base.Double(98.217)

    # decimal place input not specified to test required condition
    inputs = {"value": val}
    outputs = ["result"]
    test_data_nearest = flow.test(component_dir_nearest, inputs, outputs)
    test_data_up = flow.test(component_dir_up, inputs, outputs)
    test_data_down = flow.test(component_dir_down, inputs, outputs)

    assert check_outport_data(test_data_nearest, {"result": base.Double(98)})
    assert check_outport_data(test_data_up, {"result": base.Double(99)})
    assert check_outport_data(test_data_down, {"result": base.Double(98)})


def test_round_decimal2(flow: FlowTest):

    val = base.Double(98.217)
    dec = base.Int(2)

    # decimal place input not specified to test required condition
    inputs = {"value": val, "decimal_places": dec}
    outputs = ["result"]
    test_data_nearest = flow.test(component_dir_nearest, inputs, outputs)
    test_data_up = flow.test(component_dir_up, inputs, outputs)
    test_data_down = flow.test(component_dir_down, inputs, outputs)

    assert check_outport_data(test_data_nearest, {"result": base.Double(98.22)})
    assert check_outport_data(test_data_up, {"result": base.Double(98.22)})
    assert check_outport_data(test_data_down, {"result": base.Double(98.21)})


def test_round_decimal3(flow: FlowTest):

    val = base.Double(24.019022)
    dec = base.Int(3)

    # decimal place input not specified to test required condition
    inputs = {"value": val, "decimal_places": dec}
    outputs = ["result"]
    test_data_nearest = flow.test(component_dir_nearest, inputs, outputs)
    test_data_up = flow.test(component_dir_up, inputs, outputs)
    test_data_down = flow.test(component_dir_down, inputs, outputs)

    assert check_outport_data(test_data_nearest, {"result": base.Double(24.019)})
    assert check_outport_data(test_data_up, {"result": base.Double(24.02)})
    assert check_outport_data(test_data_down, {"result": base.Double(24.019)})


def test_round_tenths(flow: FlowTest):

    val = base.Double(1194.217)
    dec = base.Int(-1)

    # decimal place input not specified to test required condition
    inputs = {"value": val, "decimal_places": dec}
    outputs = ["result"]
    test_data_nearest = flow.test(component_dir_nearest, inputs, outputs)
    test_data_up = flow.test(component_dir_up, inputs, outputs)
    test_data_down = flow.test(component_dir_down, inputs, outputs)

    assert check_outport_data(test_data_nearest, {"result": base.Double(1190)})
    assert check_outport_data(test_data_up, {"result": base.Double(1200)})
    assert check_outport_data(test_data_down, {"result": base.Double(1190)})


def test_round_thousandths(flow: FlowTest):

    val = base.Double(1194.217)
    dec = base.Int(-3)

    # decimal place input not specified to test required condition
    inputs = {"value": val, "decimal_places": dec}
    outputs = ["result"]
    test_data_nearest = flow.test(component_dir_nearest, inputs, outputs)
    test_data_up = flow.test(component_dir_up, inputs, outputs)
    test_data_down = flow.test(component_dir_down, inputs, outputs)

    assert check_outport_data(test_data_nearest, {"result": base.Double(1000)})
    assert check_outport_data(test_data_up, {"result": base.Double(2000)})
    assert check_outport_data(test_data_down, {"result": base.Double(1000)})


if __name__ == "__main__":
    with flow_test() as flow:
        test_round_integer(flow)
        test_round_decimal2(flow)
        test_round_decimal3(flow)
        test_round_tenths(flow)
        test_round_thousandths(flow)
