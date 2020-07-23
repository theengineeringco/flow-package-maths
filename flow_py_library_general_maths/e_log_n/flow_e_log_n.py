import math

from flow import Component, LogLevel
from flow_types import base

inports = ["index", "base"]
outports = ["result"]


definition = {
    "name": "e_log_n",
    "description": "Raises an index to a power and returns the result."
    + "(Negative index values are treated as positive with negatived result).",
    "inports": [
        {"name": inports[0], "description": "The index to log, log(I, b)", "types": [base.Double]},
        {"name": inports[1], "description": "The base to log, log(i, B)", "types": [base.Double]},
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not (component.has_data(inports[0]) and component.has_data(inports[1])):
        return

    # source the data from the inports
    value1_msg: base.Double = component.get_data(inports[0])
    value2_msg: base.Double = component.get_data(inports[1])

    val1 = value1_msg.value
    val2 = value2_msg.value
    component.log(log_level=LogLevel.DEBUG, message=f"Calculating the value: {val1} log: {val2}")

    # calculate the result
    result = math.log(val1, val2)
    result_msg = base.Double(result)
    component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as addressable)
    component.send_data_addressable(result_msg, outports[0])
