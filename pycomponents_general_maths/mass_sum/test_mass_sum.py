from tec_flow import component
from tec_flow.types import base

from pycomponents_general_maths.mass_sum.mass_sum import inports, outports

import random

# Tests


def add_test_func(inputs, outputs):
    test_data = component.test(inputs, outputs)

    for port_data in test_data.values():
        assert port_data.expected == port_data.got


def test_mass_sum_doubles():
    ins1 = []
    outs = []

    for i in range(0, 5):
        in1 = random.uniform(-1000, 1000)
        outs.append(in1)
        ins1.append(base.Double(in1))

    outs = base.Double(sum(outs))

    inputs = {
        inports[0]: [ins1],
    }
    outputs = {outports[0]: outs}

    add_test_func(inputs, outputs)


if __name__ == "__main__":
    test_mass_sum_doubles()
