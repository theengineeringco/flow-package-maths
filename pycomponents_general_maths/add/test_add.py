from tec_flow import component
from tec_flow.types import base

from pycomponents_general_maths.add.add import inports, outports

import random

# Tests


def add_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)

    for port_data in test_data.values():
        assert port_data.expected == port_data.got


def test_add_ints():
    inputs = {
        inports[0]: [base.Int(1)],
        inports[1]: [base.Int(4)],
    }

    outputs = {outports[0]: [base.Double(5)]}

    add_test_func(inputs, outputs)


def test_add_int2double():
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Int(2)],
    }

    outputs = {outports[0]: [base.Double(5.67)]}

    add_test_func(inputs, outputs)


def test_add_double2double():
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(-1e9)],
    }

    outputs = {outports[0]: [base.Double((-1e9) + 3.67)]}

    add_test_func(inputs, outputs)


def test_add_array_doubles():
    ins1 = []
    ins2 = []
    outs = []

    for i in range(0, 5):
        in1 = random.uniform(-1000, 1000)
        in2 = random.uniform(-1000, 1000)
        out1 = in1 + in2
        ins1.append(base.Double(in1))
        ins2.append(base.Double(in2))
        outs.append(base.Double(out1))

    inputs = {
        inports[0]: [ins1],
        inports[1]: [ins2],
    }
    outputs = {outports[0]: [outs]}

    add_test_func(inputs, outputs)


def test_add_array_to_double():
    ins1 = []
    in2 = random.uniform(-1000, 1000)
    outs = []

    for i in range(0, 5):
        in1 = random.uniform(-1000, 1000)
        out1 = in1 + in2
        ins1.append(base.Double(in1))
        outs.append(base.Double(out1))

    inputs = {
        inports[0]: [ins1],
        inports[1]: base.Double(in2),
    }
    outputs = {outports[0]: [outs]}

    add_test_func(inputs, outputs)


if __name__ == "__main__":
    test_add_ints()
