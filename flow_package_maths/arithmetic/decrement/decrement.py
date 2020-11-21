from typing import cast

from flow import Component, Definition, Inport, Outport
from flow_types import base

# ports
value = Inport(id="value", types=[base.Int], multi_connection=False)
decrement = Inport(id="decrement", types=[base.Int], multi_connection=False)
result = Outport(id="result", types=[base.Int])

# comp definition
definition = Definition(inports=[value, decrement], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val: int = cast(base.Double, component.get_data(value)).value
    decrement_val: int = cast(base.Double, component.get_data(decrement)).value

    # add
    res = val - decrement_val

    # logs
    # component.log(log_level=LogLevel.DEBUG, message=f"Drecrement {val} by {decrement_val} gives {res}.")

    # send message to outports
    component.send_data(base.Int(res), result)
