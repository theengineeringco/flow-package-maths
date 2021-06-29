import pytest
from flow.testing import ComponentTest
from flow_types import base

component_dir = "flow_package_maths/arithmetic/divide"


@pytest.mark.parametrize(
    "numerator, denominator, result",
    [
        (base.Int(1), base.Int(1), base.Double(1)),
        (base.Int(-2), base.Int(-4), base.Double(0.5)),
        (base.Bool(False), base.Bool(True), base.Double(0)),
        (base.Double(0.99), base.Double(0.99), base.Double(1)),
        (base.Double(0), base.Double(1.5e6), base.Double(0)),
    ],
)
def test_divide_default(numerator, denominator, result):

    inports = {
        "numerator": numerator,
        "denominator": denominator,
    }

    outport = ComponentTest(component_dir).run(inports)
    assert outport["result"] == result


@pytest.mark.parametrize(
    "numerator, denominator, denominator2, result",
    [
        (base.Int(1), base.Int(1), base.Int(1), base.Double(1)),
        (base.Int(-2), base.Int(-4), base.Int(-1), base.Double(-0.5)),
        (base.Double(0.99), base.Double(0.99), base.Double(0.99), base.Double(1 / 0.99)),
        (base.Int(2), base.Bool(True), base.Double(0.2), base.Double(10)),
        (base.Double(0), base.Double(1.5e6), base.Double(-23), base.Double(0)),
    ],
)
def test_divide_terms3(numerator, denominator, denominator2, result):

    settings = {"terms": base.Int(3)}
    inports = {
        "numerator": numerator,
        "denominator": denominator,
        "denominator2": denominator2,
    }

    outport = ComponentTest(component_dir).run(inports, settings)
    assert outport["result"] == result


@pytest.mark.parametrize(
    "numerator, denominator, denominator2",
    [
        (base.Int(1), base.Int(0), base.Int(1)),
        (base.Int(1), base.Int(-2), base.Int(0)),
        (base.Double(0.99), base.Double(0.99), base.Double(0)),
        (base.Int(2), base.Bool(False), base.Double(0.2)),
    ],
)
def test_zero_division(numerator, denominator, denominator2):

    settings = {"terms": base.Int(3)}
    inports = {
        "numerator": numerator,
        "denominator": denominator,
        "denominator2": denominator2,
    }

    with pytest.raises(ZeroDivisionError):
        ComponentTest(component_dir).run(inports, settings)
