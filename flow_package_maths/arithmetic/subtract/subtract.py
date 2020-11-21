from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
value1 = Inport(id="value1", types=unions.Number, multi_connection=False)
value2 = Inport(id="value2", types=unions.Number, multi_connection=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[value1, value2], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val1: float = cast(base.Double, component.get_data(value1)).value
    val2: float = cast(base.Double, component.get_data(value2)).value

    # subtract
    res = val1 - val2

    # output message
    result_msg = base.Double(res)

    # logs
    # component.log(log_level=LogLevel.DEBUG, message=f"Subtracting {val1} by {val2} gives {res}.")

    # send message to outports
    component.send_data(result_msg, result)
