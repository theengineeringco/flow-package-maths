from flow_types import base
from pycomponents_general_maths.util.utils_tests import standard_test
from flow.testing import FlowTest, flow_test

from pycomponents_general_maths.mass_sum.flow_mass_sum import inports, outports

import random

# Tests
component_file = "pycomponents_general_maths/mass_sum/flow_mass_sum.py"


def add_test_func(inputs, outputs, flow: FlowTest):
    global component_file
    test_data = flow.test(component_file, inputs, outputs)
    standard_test(test_data)


def test_mass_sum_doubles(flow: FlowTest):
    ins1 = []
    outs = []

    for i in range(0, 5):
        in1 = random.uniform(-1000, 1000)
        outs.append(in1)
        ins1.append(base.Double(in1))

    outs = base.Double(sum(outs))

    inputs = {
        inports[0]: ins1,
    }
    outputs = {outports[0]: outs}

    add_test_func(inputs, outputs, flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_mass_sum_doubles(flow)
