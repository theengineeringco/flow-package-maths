import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "val_in, base_in, result",
    [
        [base.Double(4.5), base.Int(2), 2.1699],
        [base.Bool(True), base.Int(4), 0],
    ],
)
def test_log(val_in: FlowType, base_in: FlowType, result: float) -> None:

    inport_data = {
        "value": val_in,
        "base": base_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/logarithm/log_base").run(inport_data)

    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)


if __name__ == "__main__":
    test_log(base.Double(4.5), base.Int(2), 2.1699)
