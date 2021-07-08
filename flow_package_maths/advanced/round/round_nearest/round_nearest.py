from flow import Ports, Process
from flow_types import base

ports = Ports()
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="decimal_places", types=[base.Int, base.Bool], default=base.Int(0))
ports.add_outport(id="result", types=[base.Double])


def process(component: Process):

    value = float(component.get_data("value"))
    decimal_places = int(component.get_data("decimal_places"))

    # round nearest
    result = round(value, decimal_places)

    component.send_data(base.Double(result), "result")
