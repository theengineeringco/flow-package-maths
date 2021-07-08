from math import pi, tan

from flow import Option, Ports, Process, Settings, Setup
from flow_types import base

# define ports
ports = Ports()

# add inports
ports.add_inport(id="angle", types=[base.Double, base.Int, base.Bool])

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
        angle_conversion = pi / 180  # noqa: WPS432

    if output_type == "gradians":
        angle_conversion = pi / 200  # noqa: WPS432

    if output_type == "radians":
        angle_conversion = 1

    component.set_variable("angle_conversion", angle_conversion)


def process(component: Process):

    angle_conversion: float = component.get_variable("angle_conversion")
    angle_in = float(component.get_data("angle"))

    # sin
    angle_rad = angle_in * angle_conversion
    result = tan(angle_rad)

    component.send_data(base.Double(result), "result")
