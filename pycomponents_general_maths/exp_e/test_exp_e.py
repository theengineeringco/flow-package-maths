from tec_flow import component
from tec_flow.types import base
import pytest

from pycomponents_general_maths.exp_e.exp_e import inports, outports, exp

# Tests


def run_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)

    for port_data in test_data.values():
        for p_exp, p_got in zip(port_data.expected, port_data.got):
            assert p_exp["Value"] == pytest.approx(p_got["Value"], rel=0.000001)  # assert at least 0.00001% accurate


def test_exp_e_int():
    inputs = {
        inports[0]: [base.Int(10)],
    }

    outputs = {outports[0]: [base.Double(exp(10))]}

    run_test_func(inputs, outputs)


def test_exp_e_double():
    inputs = {
        inports[0]: [base.Double(3.67)],
    }

    outputs = {outports[0]: [base.Double(exp(3.67))]}

    run_test_func(inputs, outputs)


def test_exp_e_negatives():
    inputs = {
        inports[0]: [base.Double(-10)],
    }

    outputs = {outports[0]: [base.Double(exp(-10))]}

    run_test_func(inputs, outputs)
