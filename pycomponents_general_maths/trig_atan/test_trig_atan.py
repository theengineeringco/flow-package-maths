from tec_flow import component
from tec_flow.flow_types import base
from pycomponents_general_maths.util.utils_tests import standard_test

from pycomponents_general_maths.trig_atan.flow_trig_atan import inports, outports
import math

import random

# Tests


def run_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)
    standard_test(test_data)


def test_atan_double():
    inputs = {
        inports[0]: [base.Double(0.3)],
    }

    outputs = {outports[0]: [base.Double(math.atan(0.3))]}

    run_test_func(inputs, outputs)


def test_atan_array():
    ins1 = []
    outs = []
    for i in range(0, 5):
        in1 = random.uniform(-100, 100)
        out1 = math.atan(in1)
        ins1.append(base.Double(in1))
        outs.append(base.Double(out1))

    inputs = {
        inports[0]: [ins1],
    }
    outputs = {outports[0]: [outs]}

    run_test_func(inputs, outputs)
