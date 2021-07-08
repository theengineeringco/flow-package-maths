from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/trigonometry/acos"


@pytest.mark.parametrize(
    "settings_in, data_in, result",
    [
        ["degrees", base.Int(1), 0],
        ["degrees", base.Double(0.5), 60],
        ["degrees", base.Bool(True), 0],
        ["radians", base.Int(1), 0],
        ["radians", base.Double(0.5), 1.0472],
        ["radians", base.Bool(True), 0],
        ["gradians", base.Int(1), 0],
        ["gradians", base.Double(0.5), 66.6666],
        ["gradians", base.Bool(True), 0],
    ],
)
def test_acos(
    settings_in: str,
    data_in: Union[base.Int, base.Double, base.Bool],
    result: float,
) -> None:

    setting_values = {"angle_format": settings_in}
    inport_data = {"value": data_in}

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)
