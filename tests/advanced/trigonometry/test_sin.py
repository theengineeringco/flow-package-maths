import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "settings_in, data_in, result",
    [
        ["degrees", base.Int(80), 0.9848],
        ["degrees", base.Double(80), 0.9848],
        ["degrees", base.Bool(True), 0.0175],
        ["radians", base.Int(80), -0.9939],
        ["radians", base.Double(80), -0.9939],
        ["radians", base.Bool(True), 0.8415],
        ["gradians", base.Int(80), 0.9511],
        ["gradians", base.Double(80), 0.9511],
        ["gradians", base.Bool(True), 0.0157],
    ],
)
def test_sin(settings_in: str, data_in: FlowType, result: float) -> None:

    setting_values = {
        "rad_or_deg_or_grad": settings_in,
    }

    inport_data = {
        "angle": data_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/trigonometry/sin").run(inport_data, setting_values)

    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)


if __name__ == "__main__":
    test_sin("degrees", base.Int(80), 0.9848)
