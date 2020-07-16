import numpy as np
from flow import Component, Definition, Inport, Outport, print, run
from flow_types import base

# ---
# Component Definition
# ---
# Inports
start_port = Inport(name="start", description="The start number to begin your range from.", types=[base.Double])
stop_port = Inport(name="stop", description="The stop number to end your range from.", types=[base.Double])
num_port = Inport(name="num", description="The number of elements in your linspace stream.", types=[base.Int])

# Outports
linspace_port = Outport(
    name="linspace",
    description="The elements of your linspace stream.",
    types=[base.MdDouble],
    addressable=True,  # This is default but stated explicitly.
)

# Create definition
definition = Definition(
    name="linspace",
    description="Create a stream of values following Np Linspace procedure",
    inports=[start_port, stop_port, num_port],
    outports=[linspace_port],
)


# The process that the component performs
def process(component: Component):
    # Check that all inports have data
    if not all(component.has_data(idx.name) for idx in (start_port, stop_port, num_port)):
        return

    # source the data from the inports
    start: float = component.get_data(start_port.name).value
    stop: float = component.get_data(stop_port.name).value
    num: float = component.get_data(num_port.name).value

    array = np.linspace(start, stop, num)

    print(f"Creating linspace between {start} and {stop} with {num} elements.")
    print(f"Produced:\n{array}")

    array_msg = base.MdDouble()
    array_msg.set_array(array)

    # Send the result message to the outports (as addressable)
    component.send_data_addressable(array_msg, linspace_port.name)


if __name__ == "__main__":
    run(definition, process)
