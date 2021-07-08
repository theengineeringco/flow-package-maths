import math

from flow import Ports, Process
from flow_types import base

ports = Ports()
ports.add_inport(id="value", types=[base.Int, base.Bool])
ports.add_outport(id="result", types=[base.Int])


def process(component: Process):

    value = int(component.get_data("value"))

    result = math.factorial(value)

    component.send_data(base.Int(result), "result")
