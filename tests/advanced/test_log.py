import math
from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/log"


# User defined log base
@pytest.mark.parametrize(
    "setting, value, base_inport, result",
    [
        ["log_choice", base.Double(2.0), base.Double(10), base.Double(math.log(2.0, 10))],
        ["log_choice", base.Int(2), base.Double(10.0), base.Double(math.log(2, 10))],
        ["log_choice", base.Bool(True), base.Double(10.1), base.Double(math.log(1, 10.1))],
        ["log_choice", base.Double(2.0), base.Int(5), base.Double(math.log(2.0, 5))],
    ],
)
def test_log(
    setting: str,
    value: Union[base.Int, base.Double, base.Bool],
    base_inport: base.Double,
    result: base.Double,
) -> None:

    setting_values = {"base_choice": setting}
    inport_data = {
        "value": value,
        "base_inport": base_inport,
    }

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == result


# Natural Logarithm
@pytest.mark.parametrize(
    "setting, value, result",
    [
        ["ln_choice", base.Double(2.0), base.Double(math.log(2.0))],
        ["ln_choice", base.Int(2), base.Double(math.log(2))],
        ["ln_choice", base.Bool(True), base.Double(math.log(1))],
    ],
)
def test_ln(
    setting: str,
    value: Union[base.Int, base.Double, base.Bool],
    result: base.Double,
) -> None:

    setting_values = {"base_choice": setting}
    inport_data = {"value": value}

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)
    assert outport_data["result"] == result
