from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
value = Inport(id="value", types=unions.Number, multi_connection=False)
root = Inport(id="root", types=unions.Number, multi_connection=False, required=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[value, root], outports=[result])


def process(component: Component):

    if not component.has_data(value):
        return

    if component.has_data(root):
        root_val: float = cast(base.Double, component.get_data(root)).value
    else:
        root_val = 2

    # get inports data
    val: float = cast(base.Double, component.get_data(value)).value

    # root
    res = val ** (1 / root_val)

    # logs
    component.log(log_level=LogLevel.DEBUG, message=f"{root_val} root of {val} gives {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
