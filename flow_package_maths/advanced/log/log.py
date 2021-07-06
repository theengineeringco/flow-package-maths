import math
from typing import Union

from flow import Option, Ports, Process, Settings, Setup

# from flow.testing import ComponentTest
from flow_types import base

# Define settings
ln_choice_txt = "Natural Logarithm (e)"
log_choice_txt = "User Defined Base"

settings = Settings()
settings.add_select_setting(
    id="base_choice",
    options=[
        Option(value="ln_choice", label=ln_choice_txt),
        Option(value="log_choice", label=log_choice_txt),
    ],
    default="ln_choice",
)

# Define ports
ports = Ports()

# Add inports
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])

# Add outports
ports.add_outport(id="result", types=[base.Double])


# Setup
def setup(component: Setup):

    base_choice: str = component.get_setting("base_choice")

    if base_choice == "log_choice":
        component.add_inport(
            name="Base",
            id="base_inport",
            types=[base.Double, base.Int, base.Bool],
            default=base.Double(10),
        )
        component.set_variable("base_val", None)
    else:
        component.set_variable("base_val", math.e)


# Process
def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    # Get values for any variables set in settings
    base_val: Union[float, None] = component.get_variable("base_val")
    if base_val is None:
        base_val = float(component.get_data("base_inport"))

    # Get the data from each import
    value = float(component.get_data("value"))

    # Component Content
    if value <= 0:
        raise ValueError("The number connected to the Value inport must be greater than 0")
    elif base_val <= 0:
        raise ValueError("The number connected to the Base inport must be greater than 0")
    elif base_val == 1:
        raise ValueError("The number connected to the Base inport may not equal 1")

    # Logarithm
    value_out = math.log(value, base_val)

    # Pack the produced data into messages that will be sent from each outport
    result_msg = base.Double(value_out)

    # Send the data from each outport
    component.send_data(result_msg, "result")


# # Test
# if __name__ == "__main__":
#     setting_data = {
#         "base_choice": "ln_choice",
#         # "base_choice": "log_choice",
#     }

#     inports_data = {
#         "value": base.Double(2.0),
#         "base_inport": base.Double(10.0),
#     }

#     outport_value = ComponentTest(__file__).run(inports_data, setting_data)
#     # print(outport_value["result"])
#     assert outport_value["result"] == base.Double(math.log(2.0))
#     # assert outport_value["result"] == base.Double(math.log(2.0, 10))
