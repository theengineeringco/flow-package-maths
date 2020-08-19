from flow import Component, LogLevel
from flow_types import base

inports = ["val1", "val2"]
outports = ["result"]

definition = {
    "name": "multiply",
    "description": "Multiplies all numbers together.",
    "inports": [
        {"name": inports[0], "description": "The first number", "types": [base.Double]},
        {"name": inports[1], "description": "The second number", "types": [base.Double]},
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The actual numeric function we are performing
def multiplying_function(use_values=None):
    if use_values is None:
        use_values: dict = {"port1": 1, "port2": 2.5}
    return_value = 1
    for each in use_values.values():
        return_value *= each
    return return_value


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(all_connections=True):
        return

    # source the data from the inports
    value1_msg: base.Double = component.get_data(inports[0])
    value2_msg: base.Double = component.get_data(inports[1])

    val1 = value1_msg.value
    val2 = value2_msg.value
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Multiplying {val1} by {val2}")

    # calculate the result
    result = val1 * val2
    result_msg = base.Double(result)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as multi_connection)
    component.send_data(result_msg, outports[0])
