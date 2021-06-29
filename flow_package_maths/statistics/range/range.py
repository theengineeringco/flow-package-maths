import numpy as np
from flow import Ports, Process
from flow.testing import ComponentTest
from flow_types import base

# Ports
ports = Ports()
ports.add_inport(id="values", types=[base.MdDouble(dimension=1), base.MdInt(dimension=1), base.MdBool(dimension=1)])
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    # get inports data
    values: np.ndarray = component.get_data("values").to_ndarray()

    # explicit conversion needed since numpy ptp function doesn't work for list of bools
    values = np.array([float(value) for value in values])

    # median
    result = float(np.ptp(values))

    # send to outport
    component.send_data(base.Double(result), "result")


if __name__ == "__main__":

    inports_data = {"values": base.MdBool([True, False, True, False])}

    outport_value = ComponentTest(__file__).run(inports_data)
    print(outport_value["result"])
