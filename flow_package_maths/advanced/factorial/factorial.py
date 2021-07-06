import math

from flow import Ports, Process
from flow_types import base

# ports
ports = Ports()
ports.add_inport(id="value", types=[base.Int, base.Bool])
ports.add_outport(id="result", types=[base.Int])


def process(component: Process):

    # get inports data
    value: float = component.get_data("value")

    # root
    result = math.factorial(value)

    # send message to outports
    component.send_data(base.Int(result), "result")
