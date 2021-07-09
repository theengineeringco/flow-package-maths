from typing import Union

import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/advanced/max"


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdDouble([1]), base.Double(1)),
        (base.MdDouble([0.1, 1, 3, -4, 9.2553, 0.0422]), base.Double(9.2553)),
        (base.MdDouble([100.2, 0.1, 1, -4, 0, 100.2, -4, 0.1, 1]), base.Double(100.2)),  # repeated values
    ],
)
def test_max(values: base.MdDouble, result: base.Double) -> None:

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdInt([1, 2, 3, 4, 5, 6]), base.Double(6)),
        (base.MdInt([1, 2, 3, 4, 3, 4]), base.Double(4)),
        (base.MdBool([True, False, True, False]), base.Double(1)),
    ],
)
def test_max_other_types(values: Union[base.MdInt, base.MdBool], result: base.Double) -> None:

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result
