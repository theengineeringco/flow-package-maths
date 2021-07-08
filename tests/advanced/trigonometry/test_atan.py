from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/trigonometry/atan"


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
def test_atan(
    settings_in: str,
    data_in: Union[base.Int, base.Double, base.Bool],
    result: float,
) -> None:

    setting_values = {"angle_format": settings_in}
    inport_data = {"value": data_in}

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)
