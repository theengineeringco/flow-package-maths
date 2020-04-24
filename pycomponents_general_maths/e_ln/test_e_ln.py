from tec_flow import component
from tec_flow.types import base
import pytest

from pycomponents_general_maths.e_ln.e_ln import inports, outports
import math

# Tests


def run_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)

    for port_data in test_data.values():
        for p_exp, p_got in zip(port_data.expected, port_data.got):
            assert p_exp["Value"] == pytest.approx(p_got["Value"], rel=0.000001)  # assert at least 0.00001% accurate


def test_ln_int():
    inputs = {
        inports[0]: [base.Int(10)],
    }

    outputs = {outports[0]: [base.Double(math.log(10))]}

    run_test_func(inputs, outputs)


def test_ln_double():
    inputs = {
        inports[0]: [base.Double(3.67)],
    }

    outputs = {outports[0]: [base.Double(math.log(3.67))]}

    run_test_func(inputs, outputs)
