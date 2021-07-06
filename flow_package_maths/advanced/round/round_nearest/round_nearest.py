from typing import Any, Dict

from flow import Ports, Process
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType

ports = Ports()
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="decimal_places", types=[base.Int, base.Bool], default=base.Int(0))
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    value = float(component.get_data("value"))
    decimal_places = int(component.get_data("decimal_places"))

    # round nearest
    intermediate = round(value, decimal_places)
    if decimal_places <= 0:
        result: Any = int(intermediate)
    else:
        result = intermediate

    # send message to outports
    component.send_data(base.Double(result), "result")


if __name__ == "__main__":

    inports_data: Dict[str, FlowType] = {
        "value": base.Double(567.4354),  # noqa: WPS432
        "decimal_places": base.Int(1),
    }

    outport_value = ComponentTest(__file__).run(inports_data)
    print(outport_value["result"])
