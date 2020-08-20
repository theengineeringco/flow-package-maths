from flow import Component, LogLevel
from flow_types import base, unions

inports = ["val1", "val2"]
outports = ["result"]

definition = {
    "name": "divide",
    "description": "Divides the first number by the second number.",
    "inports": [
        {"name": inports[0], "description": "The numerator", "types": unions.Number},
        {"name": inports[1], "description": "The denominator", "types": unions.Number},
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": unions.Number}],
}


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
        component.log(log_level=LogLevel.DEBUG, message=f"Dividing {val1} by {val2}")

    # calculate the result
    result = val1 / val2
    result_msg = base.Double(result)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as multi_connection)
    component.send_data(result_msg, outports[0])
