from math import pi, tan

import numpy as np
from flow import Option, Ports, Process, Settings, Setup
from flow_types import base, unions

from flow_package_maths.advanced.trigonometry import constants

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="angle", types=unions.Number)

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

    # Get Setting Values
    output_type: str = component.get_setting("angle_format")

    if output_type == "degrees":
        angle_conversion = pi / 180  # noqa: WPS432

    if output_type == "gradians":
        angle_conversion = pi / 200  # noqa: WPS432

    if output_type == "radians":
        angle_conversion = 1

    # Set Instance Variables
    component.set_variable("angle_conversion", angle_conversion)


def process(component: Process):

    if not component.has_data():
        return

    # Get Instance Variables
    angle_conversion: float = component.get_variable("angle_conversion")

    # Get Inport Data
    angle_in = float(component.get_data("angle"))

    # Tan
    angle_rad = angle_in * angle_conversion
    if angle_rad / (pi / 2) % 2 == 1:
        # angles that are an odd multiple of pi/2 will approach infinity
        raise ValueError(
            "The Angle inport results in a tangent value that approaches infinity. "
            + "Infinity numbers aren't supported yet.",
        )

    result = tan(angle_rad)

    # Check if 'result' is a very small number which should give exactly 0
    if np.allclose(0, result, constants.rel_bound, constants.abs_bound):
        result = 0

    # Send Outport Data
    component.send_data(base.Double(result), "result")
