import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "val_in, decimal_in, result",
    [
        [base.Double(46.44), base.Int(-1), base.Double(40)],
        [base.Double(46.44), base.Int(0), base.Double(46)],
        [base.Double(46.44), base.Int(1), base.Double(46.4)],
        [base.Double(46.46), base.Int(1), base.Double(46.4)],
    ],
)
def test_round_down(val_in: FlowType, decimal_in: FlowType, result: FlowType) -> None:

    inport_data = {
        "value": val_in,
        "decimal_places": decimal_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/round/round_down").run(inport_data)

    assert outport_data["result"] == result


@pytest.mark.parametrize(
    "val_in, decimal_in, result",
    [
        [base.Double(46.44), base.Int(-1), base.Double(50)],
        [base.Double(46.44), base.Int(0), base.Double(47)],
        [base.Double(46.44), base.Int(1), base.Double(46.5)],
        [base.Double(46.46), base.Int(1), base.Double(46.5)],
    ],
)
def test_round_up(val_in: FlowType, decimal_in: FlowType, result: FlowType) -> None:

    inport_data = {
        "value": val_in,
        "decimal_places": decimal_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/round/round_up").run(inport_data)

    assert outport_data["result"] == result


@pytest.mark.parametrize(
    "val_in, decimal_in, result",
    [
        [base.Double(46.44), base.Int(-1), base.Double(50)],
        [base.Double(46.44), base.Int(0), base.Double(46)],
        [base.Double(46.44), base.Int(1), base.Double(46.4)],
        [base.Double(46.46), base.Int(1), base.Double(46.5)],
    ],
)
def test_round_nearest(val_in: FlowType, decimal_in: FlowType, result: FlowType) -> None:

    inport_data = {
        "value": val_in,
        "decimal_places": decimal_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/round/round_nearest").run(inport_data)

    assert outport_data["result"] == result


@pytest.mark.parametrize(
    "round_type, val_in, decimal_in, result",
    [
        ["nearest", base.Double(46.44), base.Int(-1), base.Double(50)],
        ["nearest", base.Double(46.44), base.Int(0), base.Double(46)],
        ["nearest", base.Double(46.44), base.Int(1), base.Double(46.4)],
        ["nearest", base.Double(46.46), base.Int(1), base.Double(46.5)],
        ["up", base.Double(46.44), base.Int(-1), base.Double(50)],
        ["up", base.Double(46.44), base.Int(0), base.Double(47)],
        ["up", base.Double(46.44), base.Int(1), base.Double(46.5)],
        ["up", base.Double(46.46), base.Int(1), base.Double(46.5)],
        ["down", base.Double(46.44), base.Int(-1), base.Double(40)],
        ["down", base.Double(46.44), base.Int(0), base.Double(46)],
        ["down", base.Double(46.44), base.Int(1), base.Double(46.4)],
        ["down", base.Double(46.46), base.Int(1), base.Double(46.4)],
    ],
)
def test_round(round_type: str, val_in: FlowType, decimal_in: FlowType, result: FlowType) -> None:

    setting_values = {
        "round_type": round_type,
    }

    inport_data = {
        "value": val_in,
        "decimal_places": decimal_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/round/round").run(inport_data, setting_values)

    assert outport_data["result"] == result


if __name__ == "__main__":
    test_round_down(base.Double(46.46), base.Int(1), base.Double(46.4))
    test_round_up(base.Double(46.46), base.Int(1), base.Double(46.5))
    test_round_nearest(base.Double(46.46), base.Int(1), base.Double(46.5))
    test_round("nearest", base.Double(46.44), base.Int(-1), base.Double(50))
