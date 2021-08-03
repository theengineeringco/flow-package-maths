from flow import Ports, Process
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])

# Add Outports
ports.add_outport(id="result", types=[base.Double])


# Process
def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    value = float(component.get_data("value"))

    out_val = abs(value)

    component.send_data(base.Double(out_val), "result")
