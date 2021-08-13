from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/log_base"


@pytest.mark.parametrize(
    "val_in, base_in, result",
    [
        [base.Double(4.5), base.Int(2), 2.1699],
        [base.Bool(True), base.Int(4), 0],
    ],
)
def test_log(
    val_in: Union[base.Double, base.Int, base.Bool],
    base_in: base.Int,
    result: float,
) -> None:

    inport_data = {
        "value": val_in,
        "base": base_in,
    }

    outport_data = ComponentTest(component_dir).run(inport_data)
    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)
