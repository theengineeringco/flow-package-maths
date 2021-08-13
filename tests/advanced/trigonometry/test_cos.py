import math
from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/trigonometry/cos"


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
def test_cos(
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
        ["degrees", base.Double(90), 0],
        ["degrees", base.Double(270), 0],
        ["radians", base.Double(math.pi / 2), 0],
        ["radians", base.Double(3 * math.pi / 2), 0],
    ],
)
def test_cos_zero_results(
    settings_in: str,
    data_in: Union[base.Int, base.Double, base.Bool],
    result: float,
) -> None:

    setting_values = {"angle_format": settings_in}
    inport_data = {"angle": data_in}

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == base.Double(result)
