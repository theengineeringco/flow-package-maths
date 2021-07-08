import math
from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/factorial"


@pytest.mark.parametrize(
    "value, result",
    [
        (base.Int(0), 1),
        (base.Int(4), math.factorial(4)),
        (base.Int(12), math.factorial(12)),
        (base.Bool(True), 1),
        (base.Bool(False), 1),
    ],
)
def test_factorial(value: Union[base.Int, base.Bool], result: int) -> None:

    inports = {"value": value}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == base.Int(result)
