import math
from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
value = Inport(id="value", types=unions.Number, multi_connection=False)
base_log = Inport(id="base", types=unions.Number, multi_connection=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[value, base_log], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val: float = cast(base.Double, component.get_data(value)).value
    base_log_val: float = cast(base.Double, component.get_data(base_log)).value

    if val < 0:
        component.log(log_level=LogLevel.ERROR, message=f"Input value is {val} which is <0. Needs to be positive.")
        return
    elif base_log_val < 0:
        component.log(log_level=LogLevel.ERROR, message=f"Input base is {val} which is <0. Needs to be positive.")
        return
    elif base_log_val == 1:
        component.log(log_level=LogLevel.ERROR, message="Input base is 1. Needs to be positive and not equal to 1.")
        return

    # logarithm
    res = math.log(val, base_log_val)

    # logs
    component.log(log_level=LogLevel.DEBUG, message=f"log_{base_log_val} of {val} gives {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)