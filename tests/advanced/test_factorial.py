import math

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/factorial"


@pytest.mark.parametrize(
    "value, result",
    [
        (base.Int(0), base.Int(1)),
        (base.Int(4), base.Int(math.factorial(4))),
        (base.Int(12), base.Int(math.factorial(12))),
        (base.Bool(True), base.Int(1)),
        (base.Bool(False), base.Int(1)),
    ],
)
def test_factorial(value, result):

    inports = {"value": value}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result
