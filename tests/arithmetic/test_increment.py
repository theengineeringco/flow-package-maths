import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType

component_dir = "flow_package_maths/arithmetic/increment"


@pytest.mark.parametrize(
    "val_in, increment_in, result",
    [
        [base.Int(2), base.Int(2), 4],
        [base.Int(2), base.Int(-1), 1],
        [base.Bool(True), base.Int(1), 2],
    ],
)
def test_increment(val_in: FlowType, increment_in: FlowType, result: int) -> None:

    inport_data = {
        "value": val_in,
        "increment": increment_in,
    }

    outport_data = ComponentTest(component_dir).run(inport_data)
    assert outport_data["result"] == base.Int(result)
