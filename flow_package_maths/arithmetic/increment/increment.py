from typing import Dict

from flow import Ports, Process
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType

ports = Ports()
ports.add_inport(id="value", types=[base.Int, base.Bool])
ports.add_inport(id="increment", types=[base.Int, base.Bool])
ports.add_outport(id="result", types=[base.Int])


def process(component: Process):

    base_val = int(component.get_data("value"))
    inc_val = int(component.get_data("increment"))

    # increment
    result = base_val + inc_val

    # send message to outports
    component.send_data(base.Int(result), "result")


if __name__ == "__main__":

    inports_data: Dict[str, FlowType] = {
        "value": base.Bool(True),
        "increment": base.Int(2),
    }

    outport_value = ComponentTest(__file__).run(inports_data)
    print(outport_value["result"])
