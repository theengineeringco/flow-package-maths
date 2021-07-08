from math import log

from flow import Ports, Process
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="base", types=[base.Double, base.Int, base.Bool], default=base.Int(10))

# add outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    value = float(component.get_data("value"))
    log_base = float(component.get_data("base"))

    if value < 0:
        raise ValueError(
            f"The number connected to the Value inport must be greater than 0. Its current value is {value}.",
        )
    elif log_base < 0:
        raise ValueError(
            "The number connected to the Base inport must be greater than 0 and not equal to 1. "
            + "Its current value is {log_base}.",
        )
    elif log_base == 1:
        raise ValueError(
            "The number connected to the Base inport must be greater than 0 and not equal to 1. "
            + "Its current value is 1.",
        )

    result = log(value, log_base)

    component.send_data(base.Double(result), "result")
