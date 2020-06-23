from pathlib import Path

from flow.testing import FlowTest, flow_test
from flow_types import base

from pycomponents_general_maths.mass_sum.flow_mass_sum import inports, outports
from pycomponents_general_maths.util.utils_tests import standard_test

# Tests
component_file = Path(__file__).parent


def add_test_func(inputs, outputs, flow: FlowTest):
    global component_file
    test_data = flow.test(component_file, inputs, outputs)
    standard_test(test_data)


def test_mass_sum_doubles(flow: FlowTest):
    ins1 = []
    outs = []

    for i in range(0, 5):
        in1 = 1.5 ** i
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
