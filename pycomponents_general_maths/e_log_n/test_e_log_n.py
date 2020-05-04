from tec_flow import component
from tec_flow.types import base
import pytest

from pycomponents_general_maths.e_log_n.flow_e_log_n import inports, outports
import math


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


def test_e_log_n_ints():
    inputs = {
        inports[0]: [base.Int(10)],
        inports[1]: [base.Int(4)],
    }

    outputs = {outports[0]: [base.Double(math.log(10, 4))]}

    run_test_func(inputs, outputs)


def test_e_log_n_double2double():
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(0.4)],
    }

    outputs = {outports[0]: [base.Double(math.log(3.67, 0.4))]}

    run_test_func(inputs, outputs)
