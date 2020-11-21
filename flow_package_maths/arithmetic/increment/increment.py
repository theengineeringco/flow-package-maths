from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base

# ports
value = Inport(id="value", types=[base.Int], multi_connection=False)
increment = Inport(id="increment", types=[base.Int], multi_connection=False)
result = Outport(id="result", types=[base.Int])

# comp definition
definition = Definition(inports=[value, increment], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val: int = cast(base.Double, component.get_data(value)).value
    increment_val: int = cast(base.Double, component.get_data(increment)).value

    # add
    res = val + increment_val

    # logs
    # component.log(log_level=LogLevel.DEBUG, message=f"Decrementing {val} by {increment_val} gives {res}.")

    # send message to outports
    component.send_data(base.Int(res), result)
