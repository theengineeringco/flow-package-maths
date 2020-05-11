from tec_flow.component import run, print, Component
from tec_flow.flow_types import base
from flow_pycomponents_utils import call_function_with_data
import math

inports = ["index", "base"]
outports = ["result"]


definition = {
    "name": "log_index_to_base",
    "description": "Raises an index to a power and returns the result. \
        (Negative index values are treated as positive with negatived result).",
    "inports": [
        {
            "name": inports[0],
            "description": "The index to log, log(I, b)",
            "types": ["base.Int", "[]base.Int", "base.Double", "[]base.Double"],
        },
        {
            "name": inports[1],
            "description": "The base to log, log(i, B)",
            "types": ["base.Int", "[]base.Int", "base.Double", "[]base.Double"],
        },
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": ["base.Double", "[]base.Double"]}],
}


# The actual numeric function we are performing
def e_log_n_function(use_values: dict = {"port1": 1, "port2": 2.5}):
    the_values = list(use_values.values())
    assert len(the_values) >= 2
    index = the_values[0]
    base_val = the_values[1]

    if base_val <= 0:
        return  # TODO: want to put in an exception here

    return math.log(index, base_val)


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not (component.has_data(inports[0]) and component.has_data(inports[1])):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])
    data2 = component.get_data(inports[1])

    val_neg = False
    if data1.value < 0:
        data1.value = -1 * data1.value
        val_neg = True

    get_data_arr = {inports[0]: data1, inports[1]: data2}
    # actually run the log function with the inputs. You can write the function explicitly instead but
    # we leverage the "call_function_with_data" as it works well for maths functions
    use_values, the_result = call_function_with_data(get_data_arr, e_log_n_function)

    if val_neg:
        use_values[0] = -1 * use_values[0]
        the_result = -1 * the_result

    if component.debug is True:
        print("{0} is {1}".format(inports, use_values))
        print("The Result of log(index, base) is {0} ".format(the_result))

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
