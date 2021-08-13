import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/statistics/average"


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdDouble([1, 2, 3, 4, 5, 6]), base.Double(21 / 6)),
        (base.MdDouble([-3, -2, -1, 0, 1, 2, 3]), base.Double(0)),
        (base.MdDouble([-1.2e3, 5.432, 0.697, 1, -0.03, 0.0101, 1000.01]), base.Double(-27.5544142857143)),
    ],
)
def test_average(values, result):

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdInt([1, 2, 3, 4, 5, 6]), base.Double(21 / 6)),
        (base.MdInt([1, -1, 2, -2, 3, -3]), base.Double(0)),
        (base.MdBool([True, False, True, False]), base.Double(0.5)),
    ],
)
def test_average_other_types(values, result):

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result
