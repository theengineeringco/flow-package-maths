from math import cos, pi
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
ports.add_inport(id="angle", types=[base.Double, base.Int, base.Bool])
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    input_type = str(component.get_setting("rad_or_deg_or_grad"))

    if input_type == degrees_name:
        angle_conversion = pi / 180  # noqa: WPS432

    if input_type == gradians_name:
        angle_conversion = pi / 200  # noqa: WPS432

    if input_type == radians_name:
        angle_conversion = 1

    component.set_variable("angle_conversion", angle_conversion)


def process(component: Process):

    angle_conversion: float = component.get_variable("angle_conversion")

    angle_in = float(component.get_data("angle"))

    angle_rad = angle_in * angle_conversion

    # cos
    result = cos(angle_rad)

    # send message to outports
    component.send_data(base.Double(result), "result")


if __name__ == "__main__":
    setting_data = {
        "rad_or_deg_or_grad": gradians_name,
    }

    inports_data = {
        "angle": base.Double(80),  # noqa: WPS432
    }

    outport_value = ComponentTest(__file__).run(inports_data, setting_data)
    print(outport_value["result"])
