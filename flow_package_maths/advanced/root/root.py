from flow import Ports, Process
from flow_types import base, unions

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=unions.Number)
ports.add_inport(id="root", types=unions.Number, default=base.Int(2))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    if not component.has_data():
        return

    # Get Inport Data
    value = float(component.get_data("value"))
    root = float(component.get_data("root"))

    if value < 0:
        raise ValueError(
            f"Value inport must be positive to give a real number. Its current value is {value} which "
            + "results in a complex number. Complex results not yet supported.",
        )

    result = value ** (1 / root)

    # Send Outport Data
    component.send_data(base.Double(result), "result")
