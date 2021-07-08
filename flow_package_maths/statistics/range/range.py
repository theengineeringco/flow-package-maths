import numpy as np
from flow import Ports, Process
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="values", types=[base.MdDouble(dimension=1), base.MdInt(dimension=1), base.MdBool(dimension=1)])

# add outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    # get data from each inport
    values: np.ndarray = component.get_data("values").to_ndarray()

    # explicit conversion needed since numpy ptp function doesn't work for list of bools
    values = np.array([float(value) for value in values])

    # range
    result = float(np.ptp(values))

    # send data to each outport
    component.send_data(base.Double(result), "result")
