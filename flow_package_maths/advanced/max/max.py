from typing import cast

import numpy as np
from flow import Component, Definition, Inport, Outport
from flow_types import base

# Ports
values = Inport(id="values", types=[base.MdDouble(dimension=1), base.MdInt(dimension=1)])
result = Outport(id="result", types=[base.Double])

# comp definition
definition = Definition(inports=[values], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    values_arr = cast(base.MdDouble, component.get_data(values)).to_ndarray()

    # range
    res = float(np.max(values_arr))

    # Log
    # component.log(log_level=LogLevel.DEBUG, message=f"Largest value in {values_arr} is {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
