import math

from flow import Ports, Process
from flow_types import base, unions

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=unions.Integer)

# Add Outports
ports.add_outport(id="result", types=[base.Int])


def process(component: Process):

    if not component.has_data():
        return

    # Get Inport Data
    value = int(component.get_data("value"))

    result = math.factorial(value)

    # Send Outport Data
    component.send_data(base.Int(result), "result")
