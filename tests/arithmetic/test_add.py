import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/arithmetic/add"


@pytest.mark.parametrize(
    "value1, value2, result",
    [
        (base.Int(1), base.Int(1), base.Double(2)),
        (base.Int(-2), base.Int(-4), base.Double(-6)),
        (base.Bool(False), base.Bool(True), base.Double(1)),
        (base.Double(0.99), base.Double(0.99), base.Double(1.98)),
        (base.Double(-1.2e6), base.Double(1.2e6), base.Double(0)),
    ],
)
def test_add_default(value1, value2, result):

    inports = {
        "value1": value1,
        "value2": value2,
    }

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result


@pytest.mark.parametrize(
    "value1, value2, value3, result",
    [
        (base.Int(1), base.Int(1), base.Int(1), base.Double(3)),
        (base.Int(-2), base.Int(-4), base.Int(-1), base.Double(-7)),
        (base.Bool(False), base.Bool(True), base.Bool(False), base.Double(1)),
        (base.Double(0.99), base.Double(0.99), base.Double(0.99), base.Double(0.99 * 3)),
        (base.Double(-1.2e6), base.Double(1.2e6), base.Double(-1.2e6), base.Double(-1.2e6)),
        (base.Int(2), base.Bool(True), base.Double(0.2), base.Double(3.2)),
    ],
)
def test_add_terms3(value1, value2, value3, result):

    settings = {"terms": base.Int(3)}
    inports = {
        "value1": value1,
        "value2": value2,
        "value3": value3,
    }

    outport = ComponentTest(component_dir).run(inports, settings)
    assert outport["result"] == result


if __name__ == "__main__":
    test_add_default(base.Int(1), base.Int(1), base.Double(2))
