from flow import Ports, Process
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="exponent", types=[base.Double, base.Int, base.Bool], default=base.Int(2))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

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

    component.send_data(base.Double(result), "result")
