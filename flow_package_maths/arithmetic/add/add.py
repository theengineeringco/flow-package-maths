from typing import List

from flow import Ports, Process, Settings, Setup
from flow_types import base

# Define Settings
settings = Settings()
settings.add_int_setting(id="terms", default=2, minimum=2, maximum=20)  # noqa: WPS 432

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value1", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="value2", types=[base.Double, base.Int, base.Bool])

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    terms: int = component.get_setting("terms")

    inport_ids: List[str] = []
    for idx in range(terms - 2):
        inport_id = f"value{idx + 3}"
        inport_ids.append(inport_id)
        component.add_inport(name=f"Value {idx + 3}", id=inport_id, types=[base.Double, base.Int, base.Bool])

    component.set_variable("inport_ids", inport_ids)


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    inport_ids: List[str] = component.get_variable("inport_ids")

    value1 = float(component.get_data("value1"))
    value2 = float(component.get_data("value2"))

    # Add all values together
    result = value1 + value2 + sum(float(component.get_data(inport_id)) for inport_id in inport_ids)

    component.send_data(base.Double(result), "result")
