import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "settings_in, data_in, result",
    [
        ["degrees", base.Int(80), 0.1736],
        ["degrees", base.Double(80), 0.1736],
        ["degrees", base.Bool(True), 0.9998],
        ["radians", base.Int(80), -0.1104],
        ["radians", base.Double(80), -0.1104],
        ["radians", base.Bool(True), 0.5403],
        ["gradians", base.Int(80), 0.3090],  # noqa: WPS339
        ["gradians", base.Double(80), 0.3090],  # noqa: WPS339
        ["gradians", base.Bool(True), 0.9999],
    ],
)
def test_cos(settings_in: str, data_in: FlowType, result: float) -> None:

    setting_values = {
        "rad_or_deg_or_grad": settings_in,
    }

    inport_data = {
        "angle": data_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/trigonometry/cos").run(inport_data, setting_values)

    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)


if __name__ == "__main__":
    test_cos("degrees", base.Int(80), 0.1736)
