import numpy as np
from flow import Ports, Process
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="values", types=[base.MdDouble(dimension=1), base.MdInt(dimension=1), base.MdBool(dimension=1)])

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    # Explicit conversion to float needed as numpy ptp function doesn't work with  bools
    values: np.ndarray = component.get_data("values").to_ndarray().astype(float)

    # Range
    result = float(np.ptp(values))

    component.send_data(base.Double(result), "result")
