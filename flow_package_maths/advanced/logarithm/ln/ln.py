import math
from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
value = Inport(id="value", types=unions.Number, multi_connection=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[value], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val: float = cast(base.Double, component.get_data(value)).value

    if val < 0:
        component.log(log_level=LogLevel.ERROR, message=f"Input value is {val} which is <0 and is invalid for ln.")
        return
    elif val == 0:
        component.log(log_level=LogLevel.ERROR, message=f"Input value is 0 which will give infinity.")
        return

    # natural log
    res = math.log(val)

    # logs
    component.log(log_level=LogLevel.DEBUG, message=f"ln({val}) gives {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
