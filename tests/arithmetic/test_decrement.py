import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "val_in, decrement_in, result",
    [
        [base.Int(2), base.Int(2), 0],
        [base.Int(2), base.Int(-1), 3],
        [base.Bool(True), base.Int(1), 0],
    ],
)
def test_decrement(val_in: FlowType, decrement_in: FlowType, result: int) -> None:

    inport_data = {
        "value": val_in,
        "decrement": decrement_in,
    }

    outport_data = ComponentTest("flow_package_maths/arithmetic/decrement").run(inport_data)

    assert outport_data["result"] == base.Int(result)


if __name__ == "__main__":
    test_decrement(base.Bool(True), base.Int(1), 0)
