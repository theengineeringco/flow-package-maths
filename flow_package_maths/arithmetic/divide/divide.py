from typing import Dict, List

from flow import IntField, Ports, Process, Settings, Setup
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType

# Ports
ports = Ports()
ports.add_outport(id="result", types=[base.Double])

# Settings
settings = Settings()
settings.add_setting(id="terms", field=IntField(min=2), default=base.Int(2))


def setup(component: Setup):

    terms = int(component.get_setting("terms"))

    # default ids and names
    inport_ids: List[str] = ["numerator", "denominator"]
    component.add_inport(name="Numerator", id=inport_ids[0], types=[base.Double, base.Int, base.Bool])
    component.add_inport(name="Denominator", id=inport_ids[1], types=[base.Double, base.Int, base.Bool])

    # additional terms will all be denominators
    for idx in range(terms - 2):
        inport_id = f"denominator{idx + 2}"
        inport_ids.append(inport_id)
        component.add_inport(name=f"Denominator {idx + 2}", id=inport_id, types=[base.Double, base.Int, base.Bool])

    component.set_variable("inport_ids", inport_ids)


def process(component: Process):

    inport_ids: List[str] = component.get_variable("inport_ids")

    numerator = float(component.get_data(inport_ids[0]))
    denominators = [float(component.get_data(inport_id)) for inport_id in inport_ids[1:]]

    if 0 in denominators:
        raise ZeroDivisionError("Divide: Zero division error.")

    # multiply all denominators together
    denominator: float = 1
    for elem in denominators:
        denominator *= elem

    result = numerator / denominator

    component.send_data(base.Double(result), "result")


if __name__ == "__main__":

    setting_data = {"terms": base.Int(2)}
    inports_data: Dict[str, FlowType] = {"numerator": base.Double(2), "denominator": base.Int(2)}

    outport_value = ComponentTest(__file__).run(inports_data, setting_data)
    print(outport_value["result"])
