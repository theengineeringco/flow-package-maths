from tec_flow import component
from tec_flow.types import base

# import pytest

from pycomponents_general_maths.trig_cos.trig_cos import inports, outports
import math

import random

# Tests


def run_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)

    for port_data in test_data.values():
        assert port_data.expected == port_data.got


def test_cos_double():
    inputs = {
        inports[0]: [base.Double(0.3)],
    }

    outputs = {outports[0]: [base.Double(math.cos(0.3))]}

    run_test_func(inputs, outputs)


def test_cos_array():
    ins1 = []
    outs = []
    for i in range(0, 5):
        in1 = random.uniform(-10, 10)
        out1 = math.cos(in1)
        ins1.append(base.Double(in1))
        outs.append(base.Double(out1))

    inputs = {
        inports[0]: [ins1],
    }
    outputs = {outports[0]: [outs]}

    run_test_func(inputs, outputs)
