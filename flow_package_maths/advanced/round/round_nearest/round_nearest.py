from typing import cast

from flow import Component, Definition, Inport, Outport
from flow_types import base, unions

# ports
value = Inport(id="value", types=unions.Number, multi_connection=False)
decimal_places = Inport(id="decimal_places", types=[base.Int], multi_connection=False, required=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[value, decimal_places], outports=[result])


def process(component: Component):

    if not component.has_data(value):
        return

    # get inports data
    val: float = cast(base.Double, component.get_data(value)).value

    if component.is_connected(decimal_places):
        dec: int = cast(base.Int, component.get_data(decimal_places)).value
    else:
        dec = 0

    # round
    res = round(val, dec)

    # Log
    # component.log(log_level=LogLevel.DEBUG, message=f"Rounding {val} to {dec} decimal places gives {res}.")

    # Create Message
    if dec == 0:
        message = base.Int(int(res))
    else:
        message = base.Double(res)

    # Send message to outports
    component.send_data(message, result)
