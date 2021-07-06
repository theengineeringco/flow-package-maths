from typing import Dict

from flow import Ports, Process
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType

ports = Ports()
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="exponent", types=[base.Double, base.Int, base.Bool], default=base.Int(2))
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    in_val = float(component.get_data("value"))
    exp_val = float(component.get_data("exponent"))

    # check for complex numbers
    if in_val < 0 and not exp_val.is_integer():
        raise ValueError(
            f"Value is negative ({in_val}) and the exponent is less than 1 ({exp_val}) which results in a "
            + "complex number. Complex numbers are not supported yet.",
        )

    # power
    result = in_val ** exp_val

    # send message to outports
    component.send_data(base.Double(result), "result")


if __name__ == "__main__":

    inports_data: Dict[str, FlowType] = {
        "value": base.Bool(True),
        "base": base.Int(4),
    }

    outport_value = ComponentTest(__file__).run(inports_data)
    print(outport_value["result"])
