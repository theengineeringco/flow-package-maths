from flow import Component, print, run
from flow_types import base

inports = ["index", "power"]
outports = ["result"]

definition = {
    "name": "idx_to_power",
    "description": "Raises an index to a power and returns the result. \
        (Negative index values are treated as positive with negatived result).",
    "inports": [
        {"name": inports[0], "description": "The index (I ^ n)", "types": [base.Int, base.Double],},
        {"name": inports[1], "description": "The power (i ^ N)", "types": [base.Int, base.Double],},
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The actual numeric function we are performing
def exp_n_function(use_values: dict = {"port1": 1, "port2": 2.5}):
    the_values = list(use_values.values())
    index = the_values[0]
    exponents = the_values[1:]
    val_neg = False
    if (
        index < 0
    ):  # TODO this is going to be fixed with imaginary numbers! It self-sorts at the minute with how some calculators do it.
        index = abs(index)
        val_neg = True

    return_value = index

    # if you provide more than 1 "n" value it'll go (i**n1)**n2**...
    for ndx in exponents:
        return_value = return_value ** ndx

    if val_neg:
        return_value = return_value * -1

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
    # actually run the exponential function with the inputs.
    the_result = exp_n_function(get_data_arr)

    print("{0} is {1}".format(inports, get_data_arr))
    print("The Result of val1 ^ val2 is {0} ".format(the_result))

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
