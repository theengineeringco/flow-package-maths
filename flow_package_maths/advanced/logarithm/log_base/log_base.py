from math import log
from typing import Dict

from flow import Ports, Process
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType

ports = Ports()
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="base", types=[base.Double, base.Int, base.Bool], default=base.Int(10))
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    in_val = float(component.get_data("value"))
    base_val = float(component.get_data("base"))

    if in_val < 0:
        raise ValueError(f"Input value is {in_val} which is <0. Needs to be positive.")
    elif base_val < 0:
        raise ValueError(f"Input base is {base_val} which is <0. Needs to be positive and not equal to 1.")
    elif base_val == 1:
        raise ValueError("Input base is 1. Needs to be positive and not equal to 1.")

    # log
    result = log(in_val, base_val)

    # send message to outports
    component.send_data(base.Double(result), "result")


if __name__ == "__main__":

    inports_data: Dict[str, FlowType] = {
        "value": base.Bool(True),
        "base": base.Int(2),
    }

    outport_value = ComponentTest(__file__).run(inports_data)
    print(outport_value["result"])
