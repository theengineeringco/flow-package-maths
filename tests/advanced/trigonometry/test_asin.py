import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "settings_in, data_in, result",
    [
        ["degrees", base.Int(1), 90],
        ["degrees", base.Double(0.5), 30],
        ["degrees", base.Bool(True), 90],
        ["radians", base.Int(1), 1.5708],
        ["radians", base.Double(0.5), 0.5236],
        ["radians", base.Bool(True), 1.5708],
        ["gradians", base.Int(1), 100],
        ["gradians", base.Double(0.5), 33.3333],
        ["gradians", base.Bool(True), 100],
    ],
)
def test_asin(settings_in: str, data_in: FlowType, result: float) -> None:

    setting_values = {
        "rad_or_deg_or_grad": settings_in,
    }

    inport_data = {
        "value": data_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/trigonometry/asin").run(inport_data, setting_values)

    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)


if __name__ == "__main__":
    test_asin("degrees", base.Double(0.5), 30)
