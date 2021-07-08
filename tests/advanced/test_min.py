from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/min"


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdDouble([1]), base.Double(1)),
        (base.MdDouble([0.1, 1, 3, -4, 9.2553, 0.0422]), base.Double(-4)),
        (base.MdDouble([100.2, 0.1, 1, -4, 0, 100.2, -4, 0.1, 1]), base.Double(-4)),  # repeated values
    ],
)
def test_min(values: base.MdDouble, result: base.Double) -> None:

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdInt([1, 2, 3, 4, 5, 6]), base.Double(1)),
        (base.MdInt([1, 2, 3, 1, 7, 1]), base.Double(1)),
        (base.MdBool([True, False, True, False]), base.Double(0)),
    ],
)
def test_min_other_types(values: Union[base.MdInt, base.MdBool], result: base.Double) -> None:

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result
