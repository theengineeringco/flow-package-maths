from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/power"


@pytest.mark.parametrize(
    "val_in, exp_in, result",
    [
        [base.Double(4.5), base.Double(2.5), 42.9567],
        [base.Bool(True), base.Int(4), 1],
    ],
)
def test_power(
    val_in: Union[base.Double, base.Int, base.Bool],
    exp_in: Union[base.Double, base.Int, base.Bool],
    result: float,
) -> None:

    inport_data = {
        "value": val_in,
        "exponent": exp_in,
    }

    outport_data = ComponentTest(component_dir).run(inport_data)
    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)
