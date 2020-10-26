from typing import cast

import numpy as np
from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
values = Inport(id="values", types=[base.MdDouble])
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[values], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    values_arr = cast(base.MdDouble, component.get_data(values)).get_array()

    # range
    res = np.min(values_arr)

    # logs
    component.log(log_level=LogLevel.DEBUG, message=f"Smallest value in {values_arr} is {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)