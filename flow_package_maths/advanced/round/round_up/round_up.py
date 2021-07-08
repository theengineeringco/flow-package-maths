from math import ceil

from flow import Ports, Process
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="decimal_places", types=[base.Int, base.Bool], default=base.Int(0))

# add outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    value = float(component.get_data("value"))
    decimal_places = int(component.get_data("decimal_places"))

    # round up
    multiplier = 10 ** decimal_places
    result = ceil(value * multiplier) / multiplier

    component.send_data(base.Double(result), "result")
