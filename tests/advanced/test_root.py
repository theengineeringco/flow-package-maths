from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/root"


@pytest.mark.parametrize(
    "val_in, root_in, result",
    [
        [base.Double(47.2), base.Double(4.5), 2.3550],  # noqa: WPS339
        [base.Bool(True), base.Int(2), 1],
    ],
)
def test_root(
    val_in: Union[base.Double, base.Int, base.Bool],
    root_in: Union[base.Double, base.Int, base.Bool],
    result: float,
) -> None:

    inport_data = {
        "value": val_in,
        "root": root_in,
    }

    outport_data = ComponentTest(component_dir).run(inport_data)
    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)
