from tec_flow import component
from tec_flow.types import base
import pytest

from pycomponents_general_maths.trig_tan.flow_trig_tan import inports, outports
import math

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


def test_tan_double():
    inputs = {
        inports[0]: [base.Double(0.3)],
    }

    outputs = {outports[0]: [base.Double(math.tan(0.3))]}

    run_test_func(inputs, outputs)


def test_tan_array():
    ins1 = []
    outs = []
    for i in range(0, 5):
        in1 = random.uniform(-100, 100)
        out1 = math.tan(in1)
        ins1.append(base.Double(in1))
        outs.append(base.Double(out1))

    inputs = {
        inports[0]: [ins1],
    }
    outputs = {outports[0]: [outs]}

    run_test_func(inputs, outputs)
