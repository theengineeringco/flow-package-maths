from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/trigonometry/asin"


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
def test_asin(
    settings_in: str,
    data_in: Union[base.Int, base.Double, base.Bool],
    result: float,
) -> None:

    setting_values = {"angle_format": settings_in}
    inport_data = {"value": data_in}

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)
