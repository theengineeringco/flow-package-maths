import math
from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/trigonometry/sin"


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
def test_sin(
    settings_in: str,
    data_in: Union[base.Int, base.Double, base.Bool],
    result: float,
) -> None:

    setting_values = {"angle_format": settings_in}
    inport_data = {"angle": data_in}

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)


@pytest.mark.parametrize(
    "settings_in, data_in, result",
    [
        ["degrees", base.Double(0), 0],
        ["degrees", base.Double(180), 0],
        ["degrees", base.Double(360), 0],
        ["radians", base.Double(math.pi), 0],
        ["radians", base.Double(2 * math.pi), 0],
    ],
)
def test_sin_zero_results(
    settings_in: str,
    data_in: Union[base.Int, base.Double, base.Bool],
    result: float,
) -> None:

    setting_values = {"angle_format": settings_in}
    inport_data = {"angle": data_in}

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == base.Double(result)
