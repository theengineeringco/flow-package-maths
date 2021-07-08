from flow import Ports, Process
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="value", types=[base.Int, base.Bool])
ports.add_inport(id="increment", types=[base.Int, base.Bool])

# add outports
ports.add_outport(id="result", types=[base.Int])


def process(component: Process):

    # get data from each inport
    value = int(component.get_data("value"))
    increment = int(component.get_data("increment"))

    # increment
    result = value + increment

    # send data to each outport
    component.send_data(base.Int(result), "result")
