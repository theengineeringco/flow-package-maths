from flow import Ports, Process
from flow_types import base, unions

# ports
ports = Ports()
ports.add_inport(id="value1", types=unions.Number)
ports.add_inport(id="value2", types=unions.Number)
ports.add_outport(id="result", types=[base.Double])


def process(component: Process) -> None:

    # get inports data
    value1: float = component.get_data("value1").value
    value2: float = component.get_data("value2").value

    # add
    result = value1 + value2

    # send message to outports
    component.send_data(base.Double(result), "result")
