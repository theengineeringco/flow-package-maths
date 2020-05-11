from tec_flow.component import run, print, Component
from tec_flow.flow_types import base
from flow_pycomponents_utils import call_function_with_data

inports = ["index", "power"]
outports = ["result"]

definition = {
    "name": "idx_to_power",
    "description": "Raises an index to a power and returns the result. \
        (Negative index values are treated as positive with negatived result).",
    "inports": [
        {
            "name": inports[0],
            "description": "The index (I ^ n)",
            "types": ["base.Int", "[]base.Int", "base.Double", "[]base.Double"],
        },
        {
            "name": inports[1],
            "description": "The power (i ^ N)",
            "types": ["base.Int", "[]base.Int", "base.Double", "[]base.Double"],
        },
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": ["base.Double", "[]base.Double"]}],
}


# The actual numeric function we are performing
def exp_n_function(use_values: dict = {"port1": 1, "port2": 2.5}):
    the_values = list(use_values.values())
    index = the_values[0]
    exponents = the_values[1:]
    val_neg = False
    if index < 0:
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

    get_data_arr = {inports[0]: data1, inports[1]: data2}
    # actually run the exponential function with the inputs. You can write the function explicitly instead but
    # we leverage the "call_function_with_data" as it works well for maths functions
    use_values, the_result = call_function_with_data(get_data_arr, exp_n_function)

    if component.debug is True:
        print("{0} is {1}".format(inports, use_values))
        print("The Result of val1 ^ val2 is {0} ".format(the_result))

    # send either a single message or an array of messages depending on how many inputs/outputs you make
    if isinstance(the_result, list):  # TODO: want to be able to remove this
        msgs = []
        for each_result in the_result:
            msgs.append(base.Double(each_result))
        component.send_data_addressable(msgs, outports[0])
    else:
        component.send_data_addressable(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
