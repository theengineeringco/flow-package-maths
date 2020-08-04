import math

from flow import Component, LogLevel
from flow_types import base

inports = ["value"]
outports = ["result"]

definition = {
    "name": "exp_n",
    "description": "Raises e to the power of n and returns the result.",
    "inports": [{"name": inports[0], "description": "The index (e ^ n)", "types": [base.Double]}],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
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
        component.log(log_level=LogLevel.DEBUG, message=f"Raising e to the power {val}")

    # calculate the results
    result = math.exp(val)
    result_msg = base.Double(result)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as addressable)
    component.send_data_addressable(result_msg, outports[0])
