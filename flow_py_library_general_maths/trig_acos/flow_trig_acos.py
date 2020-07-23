import math

from flow import Component, LogLevel
from flow_types import base, eng

inports = ["theta"]
outports = ["result"]

definition = {
    "name": "acos",
    "description": "Produces the result of acos(N) as a double",
    "inports": [{"name": inports[0], "description": "The first number", "types": [base.Double, eng.Angle]}],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(inports[0]):
        return

    # source the data from the inports
    value_msg: base.Double = component.get_data(inports[0])

    theta = value_msg.value
    component.log(log_level=LogLevel.DEBUG, message=f"Calculating acos({theta})")

    if abs(theta) > 1:
        component.log(log_level=LogLevel.ERROR, message="The result is impossible!")
        return

    # calculate the result
    result = math.acos(theta)
    result_msg = base.Double(result)
    component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as addressable)
    component.send_data_addressable(result_msg, outports[0])
