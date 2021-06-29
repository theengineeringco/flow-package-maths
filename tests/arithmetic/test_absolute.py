from typing import Union
import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/arithmetic/absolute"


@pytest.mark.parametrize(
    "value, result",
    [
        [base.Int(2), base.Double(2)],
        [base.Int(-3), base.Double(3)],
        [base.Double(2.2), base.Double(2.2)],
        [base.Double(-3.3), base.Double(3.3)],
    ],
)
def test_absolute(value: Union[base.Int, base.Double], result: base.Double) -> None:

    inport_data = {
        "value": value,
    }

    a: int
    a = "test"
    outport_data = ComponentTest(component_dir).run(inport_data)

    assert outport_data["result"] == result


if __name__ == "__main__":
    test_absolute(base.Int(-2), base.Double(2))
