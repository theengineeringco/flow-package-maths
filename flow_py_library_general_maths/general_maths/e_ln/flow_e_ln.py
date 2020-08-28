import math

from flow import Component, LogLevel
from flow_types import base, unions

inports = ["value"]
outports = ["result"]

definition = {
    "name": "natural_log",
    "description": "Natural log of the value.",
    "inports": [{"name": inports[0], "description": "The natural log of the value", "types": unions.Number}],
    "outports": [{"name": outports[0], "description": "The result number", "types": unions.Number}],
}


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(inports[0]):
        return

    # source the data from the inports
    value_msg: base.Double = component.get_data(inports[0])

    val = value_msg.value
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Getting the Natural Log of {val}")

    # calculate the results
    result = math.log(val)
    result_msg = base.Double(result)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as multi_connection)
    component.send_data(result_msg, outports[0])
