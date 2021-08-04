from math import ceil, floor

from flow import Option, Ports, Process, Settings, Setup
from flow_types import base

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
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="decimal_places", types=[base.Int, base.Bool], default=base.Int(0))

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    round_type: str = component.get_setting("round_type")
    component.set_variable("round_type", round_type)


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    round_type: str = component.get_variable("round_type")

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

    component.send_data(base.Double(result), "result")
