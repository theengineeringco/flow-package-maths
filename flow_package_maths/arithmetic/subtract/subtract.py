from typing import List

from flow import Ports, Process, Settings, Setup
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="value1", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="value2", types=[base.Double, base.Int, base.Bool])

# add outports
ports.add_outport(id="result", types=[base.Double])

# settings
settings = Settings()
settings.add_int_setting(id="terms", default=2, minimum=2)


def setup(component: Setup):

    terms: int = component.get_setting("terms")

    inport_ids: List[str] = []
    for idx in range(terms - 2):
        inport_id = f"value{idx + 3}"
        inport_ids.append(inport_id)
        component.add_inport(name=f"Value {idx + 3}", id=inport_id, types=[base.Double, base.Int, base.Bool])

    component.set_variable("inport_ids", inport_ids)


def process(component: Process):

    # get values for any variables set in settings
    inport_ids: List[str] = component.get_variable("inport_ids")

    # get data from each inport
    value1 = float(component.get_data("value1"))
    value2 = float(component.get_data("value2"))

    # subtract all values together
    result = value1 - value2 - sum(float(component.get_data(inport_id)) for inport_id in inport_ids)

    # send data to each outport
    component.send_data(base.Double(result), "result")
