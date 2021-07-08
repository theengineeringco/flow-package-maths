import numpy as np
from flow import Ports, Process
from flow_types import base

ports = Ports()
ports.add_inport(id="values", types=[base.MdDouble(dimension=1), base.MdInt(dimension=1), base.MdBool(dimension=1)])
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    values: np.ndarray = component.get_data("values").to_ndarray()

    result = float(np.max(values))

    component.send_data(base.Double(result), "result")
