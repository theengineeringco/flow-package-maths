import math
from typing import Union

from flow import Option, Ports, Process, Settings, Setup
from flow_types import base

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
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])

# Add Outports
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    base_choice: str = component.get_setting("base_choice")

    if base_choice == "log_choice":
        component.add_inport(
            name="Base",
            id="base",
            types=[base.Double, base.Int, base.Bool],
            default=base.Double(10),
        )
        component.set_variable("base_val", None)
    else:
        component.set_variable("base_val", math.e)


def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    base_val: Union[float, None] = component.get_variable("base_val")

    if base_val is None:
        base_val = float(component.get_data("base"))

    value = float(component.get_data("value"))

    if value <= 0:
        raise ValueError(
            f"The number connected to the Value inport must be greater than 0. Its current value is {value}.",
        )
    elif base_val <= 0:
        raise ValueError(
            f"The number connected to the Base inport must be greater than 0. Its current value is {base_val}.",
        )
    elif base_val == 1:
        raise ValueError(
            f"The number connected to the Base inport may not equal 1. Its current value is {base_val}.",
        )

    result = math.log(value, base_val)

    component.send_data(base.Double(result), "result")
