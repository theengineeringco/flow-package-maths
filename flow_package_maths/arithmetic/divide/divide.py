from typing import cast

from flow import Component, Definition, Inport, Outport
from flow_types import base, unions

# ports
numerator = Inport(id="numerator", types=unions.Number, multi_connection=False)
denominator = Inport(id="denominator", types=unions.Number, multi_connection=False)
result = Outport(id="result", types=[base.Double])

# comp definition
definition = Definition([numerator, denominator], [result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    num: float = cast(base.Double, component.get_data(numerator)).value
    denom: float = cast(base.Double, component.get_data(denominator)).value

    # divide
    res = num / denom

    # Log
    # component.log(log_level=LogLevel.DEBUG, message=f"Dividing {num} by {denom} gives {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
