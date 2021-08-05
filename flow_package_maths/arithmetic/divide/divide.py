from typing import List

from flow import Ports, Process, Settings, Setup
from flow_types import base, unions

# Define Settings
settings = Settings()
settings.add_int_setting(id="terms", default=2, minimum=2, maximum=20)  # noqa: WPS432


# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="numerator", types=unions.Number)
ports.add_inport(id="denominator", types=unions.Number)

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    # Get Setting Values
    terms: int = component.get_setting("terms")

    # Add Dynamic Inports
    inport_ids: List[str] = []
    for idx in range(terms - 2):
        inport_id = f"denominator{idx + 2}"
        inport_ids.append(inport_id)
        component.add_inport(name=f"Denominator {idx + 2}", id=inport_id, types=unions.Number)

    # Set Instance Variables
    component.set_variable("inport_ids", inport_ids)


def process(component: Process):

    if not component.has_data():
        return

    # Get Instance Variables
    inport_ids: List[str] = component.get_variable("inport_ids")

    # Get Inport Data
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

    # Send Outport Data
    component.send_data(base.Double(result), "result")
