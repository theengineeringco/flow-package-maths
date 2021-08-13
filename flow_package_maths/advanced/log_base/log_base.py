from math import log

from flow import Ports, Process
from flow_types import base, unions

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=unions.Number)
ports.add_inport(id="base", types=unions.Number, default=base.Int(10))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    if not component.has_data():
        return

    # Get Inport Data
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

    # Send Outport Data
    component.send_data(base.Double(result), "result")
