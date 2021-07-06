import pytest
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType


@pytest.mark.parametrize(
    "val_in, exp_in, result",
    [
        [base.Double(4.5), base.Double(2.5), 42.9567],
        [base.Bool(True), base.Int(4), 1],
    ],
)
def test_power(val_in: FlowType, exp_in: FlowType, result: float) -> None:

    inport_data = {
        "value": val_in,
        "exponent": exp_in,
    }

    outport_data = ComponentTest("flow_package_maths/advanced/power").run(inport_data)

    assert outport_data["result"] == pytest.approx(base.Double(result), abs=1e-4)


if __name__ == "__main__":
    test_power(base.Double(4.5), base.Double(2.5), 42.9567)
