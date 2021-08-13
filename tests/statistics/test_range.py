import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/statistics/range"


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdDouble([1, 2, 3, 4, 5, 6]), base.Double(5)),
        (base.MdDouble([2, 2, 2, 2]), base.Double(0)),
        (base.MdDouble([-1.2e3, 5.432, 0.697, 1, -0.03, 0.0101, 1000.01]), base.Double(2200.01)),
    ],
)
def test_range(values, result):

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdInt([3, 1, 6, 9, 13, 2]), base.Double(12)),
        (base.MdInt([1, -1, 2, -2, 3, -3]), base.Double(6)),
        (base.MdBool([True, False, True, False]), base.Double(1)),
    ],
)
def test_range_other_types(values, result):

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result
