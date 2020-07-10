from flow import Component, print, run
from flow_types import base

inports = ["val1", "val2"]
outports = ["result"]

definition = {
    "name": "add",
    "description": "Adds two numbers together.",
    "inports": [
        {"name": inports[0], "description": "The first number", "types": [base.Double]},
        {"name": inports[1], "description": "The second number", "types": [base.Double]},
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The actual numeric function we are performing
def adding_function(use_values=None):
    if use_values is None:
        use_values: dict = {"port1": 1, "port2": 2.5}
    return sum(use_values.values())


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not (component.has_data(inports[0]) and component.has_data(inports[1])):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])  # False is required to use the latest data if only one value updates
    data2 = component.get_data(inports[1])  # False is required to use the latest data if only one value updates

    get_data_arr = {inports[0]: data1.value, inports[1]: data2.value}
    # actually run the adding function with the inputs.
    the_result = adding_function(get_data_arr)

    print(f"{inports} is {get_data_arr}")
    print(f"The Result of adding these is {the_result} ")

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
