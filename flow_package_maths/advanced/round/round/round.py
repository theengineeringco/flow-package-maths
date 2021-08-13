from math import ceil, floor

from flow import Option, Ports, Process, Settings, Setup
from flow_types import base, unions

# Define Settings
settings = Settings()
settings.add_select_setting(
    id="round_type",
    options=[
        Option(value="up", label="Round Up"),
        Option(value="down", label="Round Down"),
        Option(value="nearest", label="Round to Nearest"),
    ],
    default="nearest",
)


# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=unions.Number)
ports.add_inport(id="decimal_places", types=unions.Integer, default=base.Int(0))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    # Get Setting Values
    round_type: str = component.get_setting("round_type")

    # Set Instance Variables
    component.set_variable("round_type", round_type)


def process(component: Process):

    if not component.has_data():
        return

    # Get Instance Variables
    round_type: str = component.get_variable("round_type")

    # Get Inport Data
    value = float(component.get_data("value"))
    decimal_places = int(component.get_data("decimal_places"))

    # Round - component content
    multiplier = 10 ** decimal_places
    if round_type == "nearest":
        result = round(value, decimal_places)
    elif round_type == "up":
        result = ceil(value * multiplier) / multiplier
    elif round_type == "down":
        result = floor(value * multiplier) / multiplier

    # Send Outport Data
    component.send_data(base.Double(result), "result")
