import math

from flow import Component, print, run
from flow_types import base

inports = ["value"]
outports = ["result"]

definition = {
    "name": "natural_log",
    "description": "Natural log of the value",
    "inports": [{"name": inports[0], "description": "The natural log of the value", "types": [base.Int, base.Double],}],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The actual numeric function we are performing
def ln_function(use_values: dict = {"port1": 1, "port2": 2.5}):
    ndx = list(use_values.values())[0]
    return math.log(ndx)


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(inports[0]):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])

    get_data_arr = {inports[0]: data1.value}
    the_result = ln_function(get_data_arr)

    if component.debug is True:
        print("{0} is {1}".format(inports, get_data_arr))
        print("The Result of e^value is {0} ".format(the_result))

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
