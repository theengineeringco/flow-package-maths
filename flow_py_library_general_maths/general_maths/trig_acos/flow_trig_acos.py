import math

from flow import Component, LogLevel
from flow_types import base, eng

inports = ["number"]
outports = ["result"]

definition = {
    "name": "acos",
    "description": "Produces the result of acos(n) as a double",
    "inports": [{"name": inports[0], "description": "The first number", "types": [base.Double]}],
    "outports": [{"name": outports[0], "description": "The result number", "types": [eng.Angle]}],
}


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(inports[0]):
        return

    # source the data from the inports
    value_msg: base.Double = component.get_data(inports[0])

    number = value_msg.value
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Calculating acos({number})")

    if abs(number) > 1:
        component.log(log_level=LogLevel.ERROR, message="The result is impossible!")
        return

    # calculate the result
    result = math.acos(number)
    result_msg = eng.Angle(result)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as multi_connection)
    component.send_data(result_msg, outports[0])
