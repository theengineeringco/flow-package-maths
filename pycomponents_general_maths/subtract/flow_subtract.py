from flow import Component, print, run
from flow_types import base

inports = ["val1", "val2"]
outports = ["result"]

definition = {
    "name": "subtract",
    "description": "Subtracts the second number from the first.",
    "inports": [
        {"name": inports[0], "description": "The first number", "types": [base.Int, base.Double],},
        {"name": inports[1], "description": "The second number", "types": [base.Int, base.Double],},
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The actual numeric function we are performing
def subtracting_function(use_values: dict = {"port1": 1, "port2": 2.5}):
    the_values = list(use_values.values())
    return_value = the_values[0]
    for _, each_value in enumerate(the_values[1:]):
        return_value -= each_value
    return return_value


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not (component.has_data(inports[0]) and component.has_data(inports[1])):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])
    data2 = component.get_data(inports[1])

    get_data_arr = {inports[0]: data1.value, inports[1]: data2.value}
    # actually run the subtracting function with the inputs.
    the_result = subtracting_function(get_data_arr)

    print("{0} is {1}".format(inports, get_data_arr))
    print("The Result of subtracting B from A is {0} ".format(the_result))

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
