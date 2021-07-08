from typing import List

from flow import Ports, Process, Settings, Setup
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="numerator", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="denominator", types=[base.Double, base.Int, base.Bool])

# add outports
ports.add_outport(id="result", types=[base.Double])

# Settings
settings = Settings()
settings.add_int_setting(id="terms", default=2, minimum=2)


def setup(component: Setup):

    terms: int = component.get_setting("terms")

    # additional terms will all be denominators
    inport_ids: List[str] = []
    for idx in range(terms - 2):
        inport_id = f"denominator{idx + 2}"
        inport_ids.append(inport_id)
        component.add_inport(name=f"Denominator {idx + 2}", id=inport_id, types=[base.Double, base.Int, base.Bool])

    component.set_variable("inport_ids", inport_ids)


def process(component: Process):

    # get values for any variables set in settings
    inport_ids: List[str] = component.get_variable("inport_ids")

    # get data from each inport
    numerator = float(component.get_data("numerator"))
    denominator = float(component.get_data("denominator"))
    denominators = [denominator] + [float(component.get_data(inport_id)) for inport_id in inport_ids]

    if 0 in denominators:
        raise ZeroDivisionError("The Denominator inport(s) must not be zero to prevent a zero division.")

    # multiply all denominators together
    final_denominator: float = 1
    for elem in denominators:
        final_denominator *= elem

    result = numerator / final_denominator

    component.send_data(base.Double(result), "result")
