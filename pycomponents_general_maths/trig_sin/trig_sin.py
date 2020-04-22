from tec_flow.component import run, print, Component
from tec_flow.types import base
from flow_pycomponents_utils import call_function_with_data
import math

inports = ["theta"]
outports = ["result"]

definition = {
    "name": "sin",
    "description": "Produces the result of sin(N) as a double",
    "inports": [
        {
            "name": inports[0],
            "description": "The first number",
            "types": ["base.Double", "[]base.Double", "base.Angle", "[]base.Angle"],
        },
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": ["base.Double", "[]base.Double"]}],
}


# The actual numeric function we are performing
def sin_function(use_values: dict = {"port1": 1}):
    theta = list(use_values.values())[0]
    return math.sin(theta)


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(inports[0]):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])

    get_data_arr = {inports[0]: data1}
    # actually run the sin function with the input. You can write the function explicitly instead but
    # we leverage the "call_function_with_data" as it works well for maths functions
    use_values, the_result = call_function_with_data(get_data_arr, sin_function)

    if component.debug is True:
        print("{0} is {1}".format(inports, use_values))
        print("The Result of sin(n) is {0} ".format(the_result))

    # send either a single message or an array of messages depending on how many inputs/outputs you make
    if isinstance(the_result, list):  # TODO: want to be able to remove this
        msgs = []
        for each_result in the_result:
            msgs.append(base.Double(each_result))
        component.send_data(msgs, outports[0])
    else:
        component.send_data(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
