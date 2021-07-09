from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/arithmetic/negative"


@pytest.mark.parametrize(
    "value, result",
    [
        [base.Int(2), base.Double(-2)],
        [base.Int(-3), base.Double(3)],
        [base.Double(1.5), base.Double(-1.5)],
        [base.Double(-1.6), base.Double(1.6)],
        [base.Double(0), base.Double(0)],
        [base.Bool(True), base.Double(-1.0)],
    ],
)
def test_negative(value: Union[base.Int, base.Double], result: base.Double) -> None:

    inport_data = {"value": value}

    outport_data = ComponentTest(component_dir).run(inport_data)
    assert outport_data["result"] == result
