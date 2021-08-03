from math import asin, pi

from flow import Option, Ports, Process, Settings, Setup
from flow_types import base

# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])

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
        angle_conversion = 180 / pi  # noqa: WPS432

    if output_type == "gradians":
        angle_conversion = 200 / pi  # noqa: WPS432

    if output_type == "radians":
        angle_conversion = 1

    component.set_variable("angle_conversion", angle_conversion)


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    angle_conversion: float = component.get_variable("angle_conversion")

    value = float(component.get_data("value"))

    if abs(value) > 1:
        raise ValueError(f"The Value inport must be between -1 to 1. Its current value is {value}.")

    result = asin(value)
    angle_out = result * angle_conversion

    component.send_data(base.Double(angle_out), "result")
