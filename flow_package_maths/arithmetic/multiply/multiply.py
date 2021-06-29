from typing import Dict, List

from flow import IntField, Ports, Process, Settings, Setup
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType
import math

# Ports
ports = Ports()
ports.add_outport(id="result", types=[base.Double])

# Settings
settings = Settings()
settings.add_setting(id="terms", field=IntField(min=2), default=base.Int(2))


def setup(component: Setup):

    terms = int(component.get_setting("terms"))

    inport_ids: List[str] = []
    for idx in range(terms):
        inport_id = f"value{idx + 1}"
        inport_ids.append(inport_id)
        component.add_inport(name=f"Value {idx + 1}", id=inport_id, types=[base.Double, base.Int, base.Bool])

    component.set_variable("inport_ids", inport_ids)


def process(component: Process):

    inport_ids: List[str] = component.get_variable("inport_ids")
    result = math.prod(float(component.get_data(inport_id)) for inport_id in inport_ids)

    component.send_data(base.Double(result), "result")


if __name__ == "__main__":

    setting_data = {"terms": base.Int(3)}
    inports_data: Dict[str, FlowType] = {"value1": base.Double(2), "value2": base.Int(2), "value3": base.Int(5)}

    outport_value = ComponentTest(__file__).run(inports_data, setting_data)
    print(outport_value["result"])
