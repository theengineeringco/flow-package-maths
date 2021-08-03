from math import log

from flow import Ports, Process
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="base", types=[base.Double, base.Int, base.Bool], default=base.Int(10))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

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
