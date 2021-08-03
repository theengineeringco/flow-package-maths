from flow import Ports, Process
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="decimal_places", types=[base.Int, base.Bool], default=base.Int(0))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    value = float(component.get_data("value"))
    decimal_places = int(component.get_data("decimal_places"))

    # Round nearest
    result = round(value, decimal_places)

    component.send_data(base.Double(result), "result")
