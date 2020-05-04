from tec_flow import component
from tec_flow.types import base
import pytest

from pycomponents_general_maths.exp_n.flow_exp_n import inports, outports
import random


# Tests
def run_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)
    tolerance = 0.000001
    for port_data in test_data.values():
        for p_exp, p_got in zip(port_data.expected, port_data.got):
            if isinstance(p_exp, list):
                for i in range(0, len(p_exp)):
                    p_exp[i]["Value"] == pytest.approx(p_got[i]["Value"], rel=tolerance)
            else:
                assert p_exp["Value"] == pytest.approx(
                    p_got["Value"], rel=tolerance
                )  # assert at least 0.00001% accurate


def test_exp_n_ints():
    inputs = {
        inports[0]: [base.Int(10)],
        inports[1]: [base.Int(4)],
    }

    outputs = {outports[0]: [base.Double(10 ** 4)]}

    run_test_func(inputs, outputs)


def test_exp_n_double2double():
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(-1e9)],
    }

    outputs = {outports[0]: [base.Double(3.67 ** (-1e9))]}

    run_test_func(inputs, outputs)


def test_exp_n_negatives():
    inputs = {
        inports[0]: [base.Double(-10)],
        inports[1]: [base.Double(-3)],
    }

    outputs = {outports[0]: [base.Double(-(10 ** -3))]}

    run_test_func(inputs, outputs)


def test_exp_n_array_doubles():
    ins1 = []
    ins2 = []
    outs = []

    for i in range(0, 5):
        in1 = random.uniform(-1000, 1000)
        in2 = random.uniform(-60, 60)
        if in1 >= 0:
            out1 = in1 ** in2
        else:
            out1 = -abs(in1) ** in2
        ins1.append(base.Double(in1))
        ins2.append(base.Double(in2))
        outs.append(base.Double(out1))

    inputs = {
        inports[0]: [ins1],
        inports[1]: [ins2],
    }
    outputs = {outports[0]: [outs]}

    run_test_func(inputs, outputs)
