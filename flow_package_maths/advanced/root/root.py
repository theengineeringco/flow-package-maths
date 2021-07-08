from flow import Ports, Process
from flow_types import base

ports = Ports()
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="root", types=[base.Double, base.Int, base.Bool], default=base.Int(2))
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    value = float(component.get_data("value"))
    root = float(component.get_data("root"))

    if value < 0:
        raise ValueError(
            f"Value inport must be positive to give a real number. Its current value is {value} which "
            + "results in a complex number. Complex results not yet supported.",
        )

    result = value ** (1 / root)

    component.send_data(base.Double(result), "result")
