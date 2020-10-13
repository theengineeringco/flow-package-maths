from flow.testing import FlowTest, flow_test
from flow.testing.helpers import check_outport_data
from flow_types import base

component_dir = "flow_package_maths/arithmetic/divide"


def test_divide_doubles(flow: FlowTest):

    val1 = base.Int(1)
    val2 = base.Int(1)

    inputs = {"value1": val1, "value2": val2}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Int(2)})


def test_int(flow: FlowTest):

    val1 = base.Int(1)
    val2 = base.Int(1)

    inputs = {"value1": val1, "value2": val2}
    outputs = ["result"]
    test_data = flow.test(component_dir, inputs, outputs)
    assert check_outport_data(test_data, {"result": base.Int(2)})


# def test_add_double2double(flow: FlowTest):
#     inputs = {
#         inports[0]: [base.Double(3.67)],
#         inports[1]: [base.Double(-1e9)],
#     }

#     outputs = {outports[0]: [base.Double((-1e9) + 3.67)]}

#     run_test_func(inputs, outputs, flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_add_integers(flow)


from flow.test_framework import FlowTest, flow_test
from flow.test_framework.helpers import assert_test_data_expected
from flow_types import base

from flow_package_maths.general_maths.divide.flow_divide import inports, outports

# Tests
component_file = "maths/divide"


def run_test_func(inputs, outputs, flow: FlowTest):
    test_data = flow.test(component_file, inputs, outputs)
    assert_test_data_expected(test_data)


def test_divide_double2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Double(3.67)],
        inports[1]: [base.Double(-1e9)],
    }

    outputs = {outports[0]: [base.Double(3.67 / (-1e9))]}

    run_test_func(inputs, outputs, flow=flow)


def test_divide_int2double(flow: FlowTest):
    inputs = {
        inports[0]: [base.Int(1000)],
        inports[1]: [base.Int(255)],
    }

    outputs = {outports[0]: [base.Double(3.9215686274509802)]}

    run_test_func(inputs, outputs, flow=flow)


if __name__ == "__main__":
    with flow_test() as flow:
        test_divide_double2double(flow)
        test_divide_int2double(flow)
