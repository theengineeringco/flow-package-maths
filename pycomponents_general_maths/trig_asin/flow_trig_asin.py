import math

from flow import Component, print, run
from flow_types import base, eng

inports = ["theta"]
outports = ["result"]

definition = {
    "name": "asin",
    "description": "Produces the result of asin(N) as a double",
    "inports": [{"name": inports[0], "description": "The first number", "types": [base.Double, eng.Angle],},],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The actual numeric function we are performing
def asin_function(use_values: dict = {"port1": 1}):
    theta_val = list(use_values.values())[0]
    if abs(theta_val) > 1:
        raise ArithmeticError(
            "You cannot operate {0} with this value of theta of {1}".format(definition["name"], theta_val)
        )

    return math.asin(theta_val)


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(inports[0]):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])

    get_data_arr = {inports[0]: data1.value}
    # actually run the asin function with the input.
    the_result = asin_function(get_data_arr)

    print("{0} is {1}".format(inports, get_data_arr))
    print("The Result of asin(n) is {0} ".format(the_result))

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
