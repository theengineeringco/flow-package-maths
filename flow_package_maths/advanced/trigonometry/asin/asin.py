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
    # note angle_val is in radians
    val: float = cast(base.Double, component.get_data(value)).value

    if abs(val) > 1:
        component.log(log_level=LogLevel.ERROR, message=f"Input value is {val}, which needs to be between -1 to 1.")
        return

    # asin
    res = math.asin(val)

    # logs
    res_deg = res * 180 / math.pi
    component.log(log_level=LogLevel.DEBUG, message=f"asin({val}) gives {res}rad or {res_deg}°.")

    # send message to outports
    component.send_data(base.Double(res), result)
