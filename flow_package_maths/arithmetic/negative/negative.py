from typing import cast

from flow import Component, Definition, Inport, Outport
from flow_types import base, unions

# ports
value = Inport(id="value", types=unions.Number, multi_connection=False)
result = Outport(id="result", types=[base.Double])

# comp definition
definition = Definition(inports=[value], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val: float = cast(base.Double, component.get_data(value)).value

    # negative
    res = -val

    # Log
    # component.log(log_level=LogLevel.DEBUG, message=f"Negative of {val} is {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
