import math
from typing import Optional

from flow import Option, Ports, Process, Settings, Setup
from flow_types import base, unions

# Define Settings
settings = Settings()
settings.add_select_setting(
    id="base_choice",
    options=[
        Option(value="ln_choice", label="Natural Logarithm (e)"),
        Option(value="log_choice", label="Custom Defined Base"),
    ],
    default="ln_choice",
)


# Define Ports
ports = Ports()

# Add Inports
ports.add_inport(id="value", types=unions.Number)

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    # Get Setting Values
    base_choice: str = component.get_setting("base_choice")

    base_value: Optional[float]
    if base_choice == "log_choice":
        component.add_inport(name="Base", id="base", types=unions.Number, default=base.Double(10))
        base_value = None
    else:
        base_value = math.e

    # Set Instance Variables
    component.set_variable("base_value", base_value)


def process(component: Process):

    if not component.has_data():
        return

    # Get Instance Variables
    base_value: Optional[float] = component.get_variable("base_value")

    # Get Inport Data
    value = float(component.get_data("value"))
    if base_value is None:
        base_value = float(component.get_data("base"))

    if value <= 0:
        raise ValueError(
            f"The number connected to the Value inport must be greater than 0. Its current value is {value}.",
        )
    elif base_value <= 0:
        raise ValueError(
            f"The number connected to the Base inport must be greater than 0. Its current value is {base_value}.",
        )
    elif base_value == 1:
        raise ValueError(
            f"The number connected to the Base inport may not equal 1. Its current value is {base_value}.",
        )

    result = math.log(value, base_value)

    # Send Outport Data
    component.send_data(base.Double(result), "result")
