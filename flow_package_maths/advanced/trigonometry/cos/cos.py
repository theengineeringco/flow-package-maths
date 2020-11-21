import math
from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
angle = Inport(id="angle", types=unions.Number, multi_connection=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[angle], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    # note angle_val is in radians
    angle_val: float = cast(base.Double, component.get_data(angle)).value

    # cos
    res = math.cos(angle_val)

    # logs
    angle_val_deg = angle_val * 180 / math.pi  # noqa: WPS432
    # component.log(log_level=LogLevel.DEBUG, message=f"cos({angle_val}rad or {angle_val_deg}°) gives {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
