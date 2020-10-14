import math
from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
value = Inport(id="value", types=unions.Number, multi_connection=False)
decimal_places = Inport(id="decimal_places", types=[base.Int], multi_connection=False, required=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[value], outports=[result])


def process(component: Component):

    if not component.has_data(value):
        return

    # get inports data
    val: float = cast(base.Double, component.get_data(value)).value

    if component.has_data(decimal_places):
        dec: int = cast(base.Int, component.get_data(decimal_places)).value
    else:
        dec = 0

    # round up
    res = int(math.ceil(val / 10 ** -dec)) * 10 ** -dec

    # logs
    component.log(log_level=LogLevel.DEBUG, message=f"Rounding up {val} to {dec} decimal places gives {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
