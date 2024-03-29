import math
from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/trigonometry/tan"


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
def test_tan(
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
def test_tan_zero_results(
    settings_in: str,
    data_in: base.Double,
    result: float,
) -> None:

    setting_values = {"angle_format": settings_in}
    inport_data = {"angle": data_in}

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == base.Double(result)


@pytest.mark.parametrize(
    "settings_in, data_in",
    [
        ["degrees", base.Double(90)],
        ["degrees", base.Double(270)],
        ["radians", base.Double(math.pi / 2)],
        ["radians", base.Double(3 * math.pi / 2)],
    ],
)
def test_tan_infinity_results(
    settings_in: str,
    data_in: base.Double,
) -> None:

    setting_values = {"angle_format": settings_in}
    inport_data = {"angle": data_in}

    with pytest.raises(ValueError):
        ComponentTest(component_dir).run(inport_data, setting_values)
