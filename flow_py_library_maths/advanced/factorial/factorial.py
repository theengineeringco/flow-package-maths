import math
from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base

# ports
value = Inport(id="value", types=[base.Int], multi_connection=False)
result = Outport(id="result", types=[base.Int])

# comp definition
definition = Definition(inports=[value], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val: float = cast(base.Double, component.get_data(value)).value

    # root
    res = math.factorial(val)

    # logs
    component.log(log_level=LogLevel.DEBUG, message=f"{val}! gives {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
