from math import pi, sin

import numpy as np
from flow import Option, Ports, Process, Settings, Setup
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="angle", types=[base.Double, base.Int, base.Bool])

# Add Outports
ports.add_outport(id="result", types=[base.Double])

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

    output_type: str = component.get_setting("angle_format")

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

    # Sin
    angle_rad = angle_in * angle_conversion
    result = sin(angle_rad)

    # check if 'result' is a very small number which should give exactly 0
    rel_bound = 1e-5
    abs_bound = 1e-8
    if np.allclose(0, result, rel_bound, abs_bound):
        result = 0

    component.send_data(base.Double(result), "result")
