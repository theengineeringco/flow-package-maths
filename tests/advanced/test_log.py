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
        [base.String("User Defined Base"), base.Double(2.0), base.Double(10), base.Double(math.log(2.0, 10))],
        [base.String("User Defined Base"), base.Int(2), base.Double(10.0), base.Double(math.log(2, 10))],
        [base.String("User Defined Base"), base.Bool(True), base.Double(10.1), base.Double(math.log(1, 10.1))],
        [base.String("User Defined Base"), base.Double(2.0), base.Int(5), base.Double(math.log(2.0, 5))],
    ],
)
def test_log(
    setting: base.String,
    value: Union[base.Int, base.Double, base.Bool],
    base_inport: base.Double,
    result: base.Double,
) -> None:

    setting_values = {
        "base_choice": setting,
    }

    inport_data = {
        "value": value,
        "base_inport": base_inport,
    }

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)

    # print(outport_data["result"])
    assert outport_data["result"] == result


# Natural Logarithm
@pytest.mark.parametrize(
    "setting, value, result",
    [
        [base.String("Natural Logarithm (e)"), base.Double(2.0), base.Double(math.log(2.0))],
        [base.String("Natural Logarithm (e)"), base.Int(2), base.Double(math.log(2))],
        [base.String("Natural Logarithm (e)"), base.Bool(True), base.Double(math.log(1))],
    ],
)
def test_ln(
    setting: base.String,
    value: Union[base.Int, base.Double, base.Bool],
    result: base.Double,
) -> None:

    setting_values = {
        "base_choice": setting,
    }

    inport_data = {
        "value": value,
    }

    outport_data = ComponentTest(component_dir).run(inport_data, setting_values)

    # print(outport_data["result"])
    assert outport_data["result"] == result


if __name__ == "__main__":
    test_log(base.String("User Defined Base"), base.Double(2.0), base.Double(10), base.Double(math.log(2.0, 10)))
    test_ln(base.String("Natural Logarithm (e)"), base.Double(2.0), base.Double(math.log(2.0)))
