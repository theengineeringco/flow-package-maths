from pathlib import Path
from typing import List

import pytest
from flow.testing import FlowTest, flow_test
from flow_types import base

from flow_py_library_general_maths.array.assemble.linspace.flow_linspace import (
    linspace_port,
    num_port,
    start_port,
    stop_port,
)
from flow_py_library_general_maths.util.utils_tests import basic_test_eval

# Tests

component_file = Path(__file__).parent


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs, timeout=1000)
    basic_test_eval(test_data)


@pytest.mark.parametrize(
    ("start", "stop", "num", "result"),
    [
        (base.Double(0), base.Double(10), base.Int(6), [0, 2, 4, 6, 8, 10]),
        (
            base.Double(0.5),
            base.Double(1),
            base.Int(11),
            [0.5 + ((1.05 - 0.5) * float(idx) / float(11)) for idx in range(11)],
        ),
    ],  # We can test this function multiple times with different values
)
def test_linspace(start: base.Double, stop: base.Double, num: base.Double, result: List[float], flow: FlowTest):
    inputs = {
        start_port.name: start,
        stop_port.name: stop,
        num_port.name: num,
    }
    array_msg = base.MdDouble()
    array_msg.set_array(result)
    outputs = {linspace_port.name: array_msg}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_linspace(
            start=base.Double(0),
            stop=base.Double(10),
            num=base.Int(6),
            result=[0, 2, 4, 6, 8, 10],
            flow=flow,
        )
