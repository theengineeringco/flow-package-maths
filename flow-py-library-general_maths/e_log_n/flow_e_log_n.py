import math

from flow import Component, print, run
from flow_types import base

inports = ["index", "base"]
outports = ["result"]


definition = {
    "name": "log_index_to_base",
    "description": "Raises an index to a power and returns the result. \
        (Negative index values are treated as positive with negatived result).",
    "inports": [
        {"name": inports[0], "description": "The index to log, log(I, b)", "types": [base.Int, base.Double],},
        {"name": inports[1], "description": "The base to log, log(i, B)", "types": [base.Int, base.Double],},
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The actual numeric function we are performing
def e_log_n_function(use_values: dict = {"port1": 1, "port2": 2.5}):
    the_values = list(use_values.values())
    assert len(the_values) >= 2
    index = the_values[0]
    base_val = the_values[1]

    if base_val <= 0:
        raise Exception("You cannot have a base value <= 0.")

    return math.log(index, base_val)


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not (component.has_data(inports[0]) and component.has_data(inports[1])):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])
    data2 = component.get_data(inports[1])

    get_data_arr = {inports[0]: data1.value, inports[1]: data2.value}
    # actually run the log function with the inputs.
    the_result = e_log_n_function(get_data_arr)

    print("{0} is {1}".format(inports, get_data_arr))
    print("The Result of log(index, base) is {0} ".format(the_result))

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
