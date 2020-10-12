import math

from flow import Component, LogLevel
from flow_types import base, eng, unions

inports = ["theta"]
outports = ["result"]

definition = {
    "name": "tan",
    "description": "Produces the result of tan(theta) as a double",
    "inports": [{"name": inports[0], "description": "The first number", "types": [eng.Angle]}],
    "outports": [{"name": outports[0], "description": "The result number", "types": unions.Number}],
}


# The process that the component performs
def process(component: Component) -> None:
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data():
        return

    # source the data from the inports
    value_msg: base.Double = component.get_data(inports[0])

    theta = value_msg.value
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Calculating tan({theta})")

    # calculate the result
    result = math.tan(theta)
    result_msg = base.Double(result)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as multi_connection)
    component.send_data(result_msg, outports[0])
