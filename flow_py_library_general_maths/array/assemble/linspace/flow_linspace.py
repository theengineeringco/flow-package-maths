import numpy as np
from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ---
# Component Definition
# ---
# Inports
start_port = Inport(name="start", description="The start number to begin your range from.", types=unions.Number)
stop_port = Inport(name="stop", description="The stop number to end your range from.", types=unions.Number)
num_port = Inport(name="num", description="The number of elements in your linspace stream.", types=[base.Int])

# Outports
linspace_port = Outport(
    name="linspace",
    description="The elements of your linspace stream.",
    types=[base.MdDouble],
    multi_connection=True,  # This is default but stated explicitly.
)

# Create definition
definition = Definition(
    name="linspace",
    description="Create a List of values following Np Linspace procedure",
    inports=[start_port, stop_port, num_port],
    outports=[linspace_port],
)


# The process that the component performs
def process(component: Component):
    # Check that all inports have data
    if not component.has_data():
        return

    # source the data from the inports
    start: float = component.get_data(start_port).value
    stop: float = component.get_data(stop_port).value
    num: float = component.get_data(num_port).value
    if component.debug:
        component.log(
            log_level=LogLevel.DEBUG, message=f"Creating linspace between {start} and {stop} with {num} elements.",
        )

    array = np.linspace(start, stop, num)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Produced:\n{array}")

    array_msg = base.MdDouble()
    array_msg.set_array(array)

    # Send the result message to the outports (as multi_connection)
    component.send_data(array_msg, linspace_port)
