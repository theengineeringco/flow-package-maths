from typing import List

from flow import Ports, Process, Settings, Setup
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="numerator", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="denominator", types=[base.Double, base.Int, base.Bool])

# Add Outports
ports.add_outport(id="result", types=[base.Double])

# Define Settings
settings = Settings()
settings.add_int_setting(id="terms", default=2, minimum=2)


def setup(component: Setup):

    terms: int = component.get_setting("terms")

    # Additional terms will all be denominators
    inport_ids: List[str] = []
    for idx in range(terms - 2):
        inport_id = f"denominator{idx + 2}"
        inport_ids.append(inport_id)
        component.add_inport(name=f"Denominator {idx + 2}", id=inport_id, types=[base.Double, base.Int, base.Bool])

    component.set_variable("inport_ids", inport_ids)


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    inport_ids: List[str] = component.get_variable("inport_ids")

    numerator = float(component.get_data("numerator"))
    denominator = float(component.get_data("denominator"))
    denominators = [denominator] + [float(component.get_data(inport_id)) for inport_id in inport_ids]

    if 0 in denominators:
        raise ZeroDivisionError("The Denominator inport(s) must not be zero to prevent a zero division.")

    # Multiply all denominators together
    final_denominator: float = 1
    for elem in denominators:
        final_denominator *= elem

    result = numerator / final_denominator

    component.send_data(base.Double(result), "result")
