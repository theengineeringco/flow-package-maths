from tec_flow.component import run, print, Component
from tec_flow.flow_types import base
from flow_pycomponents_utils import call_function_with_data

inports = ["val1", "val2"]
outports = ["result"]

definition = {
    "name": "add",
    "description": "Adds two numbers together.",
    "inports": [
        {
            "name": inports[0],
            "description": "The first number",
            "types": ["base.Int", "[]base.Int", "base.Double", "[]base.Double"],
        },
        {
            "name": inports[1],
            "description": "The second number",
            "types": ["base.Int", "[]base.Int", "base.Double", "[]base.Double"],
        },
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": ["base.Double", "[]base.Double"]}],
}


# The actual numeric function we are performing
def adding_function(use_values: dict = {"port1": 1, "port2": 2.5}):
    return_value = 0
    for each in use_values.values():
        return_value += each
    return return_value


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not (component.has_data(inports[0]) and component.has_data(inports[1])):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])  # False is required to use the latest data if only one value updates
    data2 = component.get_data(inports[1])  # False is required to use the latest data if only one value updates

    get_data_arr = {inports[0]: data1, inports[1]: data2}
    # actually run the adding function with the inputs. You can write the function explicitly instead but
    # we leverage the "call_function_with_data" as it works well for maths functions
    use_values, the_result = call_function_with_data(get_data_arr, adding_function)

    if component.debug is True:
        print("{0} is {1}".format(inports, use_values))
        print("The Result of adding these is {0} ".format(the_result))

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
