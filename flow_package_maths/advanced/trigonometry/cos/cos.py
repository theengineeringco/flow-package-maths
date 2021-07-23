from math import cos, pi

import numpy as np
from flow import Option, Ports, Process, Settings, Setup
from flow_types import base

from flow_package_maths.advanced.trigonometry import constants

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="angle", types=[base.Double, base.Int, base.Bool])

# Add Outports
ports.add_outport(id="result", types=[base.Double])

# Define Settings
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

    # Check all connected inports have data
    if not component.has_data():
        return

    angle_conversion: float = component.get_variable("angle_conversion")

    angle_in = float(component.get_data("angle"))

    # Cos
    angle_rad = angle_in * angle_conversion
    result = cos(angle_rad)

    # Check if 'result' is a very small number which should give exactly 0
    if np.allclose(0, result, constants.rel_bound, constants.abs_bound):
        result = 0

    component.send_data(base.Double(result), "result")
