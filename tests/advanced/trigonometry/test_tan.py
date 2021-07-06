import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "settings_in, data_in, result",
    [
        ["degrees", base.Int(80), 5.6713],
        ["degrees", base.Double(80), 5.6713],
        ["degrees", base.Bool(True), 0.0175],
        ["radians", base.Int(80), 9.0037],
        ["radians", base.Double(80), 9.0037],
        ["radians", base.Bool(True), 1.5574],
        ["gradians", base.Int(80), 3.0777],
        ["gradians", base.Double(80), 3.0777],
        ["gradians", base.Bool(True), 0.0157],
    ],
)
def test_tan(settings_in: str, data_in: FlowType, result: float) -> None:

    setting_values = {
        "rad_or_deg_or_grad": settings_in,
    }

    inport_data = {
        "angle": data_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/trigonometry/tan").run(inport_data, setting_values)

    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)


if __name__ == "__main__":
    test_tan("degrees", base.Int(80), 5.6713)
