from math import atan, pi

from flow import Option, Ports, Process, Settings, Setup
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])

# add outports
ports.add_outport(id="result", types=[base.Double])

# settings
settings = Settings()
settings.add_select_setting(
    id="angle_format",
    options=[
        Option("degrees", "Degrees"),
        Option("radians", "Radians"),
        Option("gradians", "Gradians"),
    ],
    default="radians",
)


def setup(component: Setup):

    output_type = str(component.get_setting("angle_format"))

    if output_type == "degrees":
        angle_conversion = 180 / pi  # noqa: WPS432

    if output_type == "gradians":
        angle_conversion = 200 / pi  # noqa: WPS432

    if output_type == "radians":
        angle_conversion = 1

    component.set_variable("angle_conversion", angle_conversion)


def process(component: Process):

    angle_conversion: float = component.get_variable("angle_conversion")

    value = float(component.get_data("value"))

    result = atan(value)
    angle_out = result * angle_conversion

    component.send_data(base.Double(angle_out), "result")
