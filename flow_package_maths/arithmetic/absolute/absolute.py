from flow import Ports, Process
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])

# add outports
ports.add_outport(id="result", types=[base.Double])


# Process
def process(component: Process):

    # Get the data from each import
    value = float(component.get_data("value"))

    # Component Content
    out_val = abs(value)

    # Send the data from each outport
    component.send_data(base.Double(out_val), "result")
