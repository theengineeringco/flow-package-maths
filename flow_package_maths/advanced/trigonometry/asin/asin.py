from math import asin, pi
from typing import List

from flow import Ports, Process, Settings, Setup
from flow.definitions.settings.setting import Option
from flow.testing import ComponentTest
from flow_types import base

degrees_name = "degrees"
radians_name = "radians"
gradians_name = "gradians"

input_types: List[Option] = [
    Option(degrees_name, "Degrees"),
    Option(radians_name, "Radians"),
    Option(gradians_name, "Gradians"),
]

settings = Settings()
settings.add_select_setting(id="rad_or_deg_or_grad", options=input_types, default=radians_name)

ports = Ports()
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    output_type = str(component.get_setting("rad_or_deg_or_grad"))

    if output_type == degrees_name:
        angle_conversion = 180 / pi  # noqa: WPS432

    if output_type == gradians_name:
        angle_conversion = 200 / pi  # noqa: WPS432

    if output_type == radians_name:
        angle_conversion = 1

    component.set_variable("angle_conversion", angle_conversion)


def process(component: Process):

    angle_conversion: float = component.get_variable("angle_conversion")

    value_in = float(component.get_data("value"))

    if abs(value_in) > 1:
        raise ValueError(f"Input value is {value_in}, which needs to be between -1 to 1.")

    # asin
    result = asin(value_in)

    angle_out = result * angle_conversion

    # send message to outports
    component.send_data(base.Double(angle_out), "result")


if __name__ == "__main__":
    setting_data = {
        "rad_or_deg_or_grad": degrees_name,
    }

    inports_data = {
        "value": base.Double(0.5),
    }

    outport_value = ComponentTest(__file__).run(inports_data, setting_data)
    print(outport_value["result"])
