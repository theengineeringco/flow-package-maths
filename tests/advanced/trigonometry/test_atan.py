import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "settings_in, data_in, result",
    [
        ["degrees", base.Int(1), 45],
        ["degrees", base.Double(0.5), 26.5651],
        ["degrees", base.Bool(True), 45],
        ["radians", base.Int(1), 0.7854],
        ["radians", base.Double(0.5), 0.4636],
        ["radians", base.Bool(True), 0.7854],
        ["gradians", base.Int(1), 50],
        ["gradians", base.Double(0.5), 29.5168],
        ["gradians", base.Bool(True), 50],
    ],
)
def test_atan(settings_in: str, data_in: FlowType, result: float) -> None:

    setting_values = {
        "rad_or_deg_or_grad": settings_in,
    }

    inport_data = {
        "value": data_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/trigonometry/atan").run(inport_data, setting_values)

    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)


if __name__ == "__main__":
    test_atan("degrees", base.Double(0.5), 0.9848)
