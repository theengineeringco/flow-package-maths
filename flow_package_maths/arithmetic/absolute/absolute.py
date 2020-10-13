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
    val: float = cast(base.Double, component.get_data(value)).value

    # absolute
    res = abs(val)

    # output message
    result_msg = base.Double(res)

    # logs
    component.log(log_level=LogLevel.DEBUG, message=f"Absolute of {val} is {res}.")

    # send message to outports
    component.send_data(result_msg, result)
