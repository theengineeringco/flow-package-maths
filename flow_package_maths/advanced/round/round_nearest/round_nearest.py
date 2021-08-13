from flow import Ports, Process
from flow_types import base, unions

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=unions.Number)
ports.add_inport(id="decimal_places", types=unions.Integer, default=base.Int(0))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    if not component.has_data():
        return

    # Get Inport Data
    value = float(component.get_data("value"))
    decimal_places = int(component.get_data("decimal_places"))

    # Round nearest
    result = round(value, decimal_places)

    # Send Outport Data
    component.send_data(base.Double(result), "result")
