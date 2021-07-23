import math

from flow import Ports, Process
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=[base.Int, base.Bool])

# Add Outports
ports.add_outport(id="result", types=[base.Int])


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    value = int(component.get_data("value"))

    result = math.factorial(value)

    component.send_data(base.Int(result), "result")
