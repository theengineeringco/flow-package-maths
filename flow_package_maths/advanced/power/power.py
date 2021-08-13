from flow import Ports, Process
from flow_types import base, unions

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=unions.Number)
ports.add_inport(id="exponent", types=unions.Number, default=base.Int(2))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    if not component.has_data():
        return

    # Get Inport Data
    value = float(component.get_data("value"))
    exponent = float(component.get_data("exponent"))

    result = value ** exponent

    # Check if result has a imaginary part
    if result.imag:
        raise ValueError(
            "The Value inport must be positive and the Exponent inport must be more than 1 to give a real number. "
            + f"Their current values are {value} and {exponent} correspondingly which results in a complex number. "
            + "Complex numbers are not supported yet.",
        )

    # Send Outport Data
    component.send_data(base.Double(result), "result")
