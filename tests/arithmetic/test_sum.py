import numpy as np
import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/arithmetic/sum"


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdDouble(list(np.linspace(0, 10, 11))), base.Double(11 * 10 / 2)),
        (base.MdDouble([-3, -2, -1, 0, 1, 2, 3]), base.Double(0)),
        (base.MdDouble([-1.2e3, 5.432, 0.697, 1, -0.03, 0.0101, 1000.01]), base.Double(-192.8809000000001)),
    ],
)
def test_sum(values, result):

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result


@pytest.mark.parametrize(
    "values, result",
    [
        (base.MdInt([1, 2, 3, 4, 5, 6]), base.Double(21)),
        (base.MdInt([1, -1, 2, -2, 3, -3]), base.Double(0)),
        (base.MdBool([True, False, True, False]), base.Double(2)),
    ],
)
def test_sum_other_types(values, result):

    inports = {"values": values}

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result
