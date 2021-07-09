from flow import Ports, Process
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=[base.Int, base.Bool])
ports.add_inport(id="decrement", types=[base.Int, base.Bool])

# Add Outports
ports.add_outport(id="result", types=[base.Int])


def process(component: Process):

    value = int(component.get_data("value"))
    decrement = int(component.get_data("decrement"))

    # Increment
    result = value - decrement

    component.send_data(base.Int(result), "result")
