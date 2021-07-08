from flow import Ports, Process
from flow_types import base

# Define ports
ports = Ports()

# Add inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])

# Add outports
ports.add_outport(id="result", types=[base.Double])


# Process
def process(component: Process):

    # Get the data from each import
    value: float = component.get_data("value").value

    # Component Content
    out_val = -value

    # Send the data to each outport
    component.send_data(base.Double(out_val), "result")
