import numpy as np
from flow import Component, LogLevel
from flow_types import base

inports = ["array", "shape"]
outports = ["result_array"]

definition = {
    "name": "reshape_array",
    "description": "Reshape an MdDouble array to a new shape provided as an MdInt.",
    "inports": [
        {"name": inports[0], "description": "The array", "types": [base.MdDouble]},
        {"name": inports[1], "description": "The shape as a 1D array", "types": [base.MdInt]},
        {"name": "strict", "description": "Do not allow resizing.", "types": [base.Bool], "required": False},
    ],  # TODO these will also be used for MdArrays. Need a consistent way, or do we have specific versions?
    "outports": [{"name": outports[0], "description": "The reshaped array", "types": [base.MdDouble]}],
    # We enforce doubles for maths
}


# The process that the component performs
def process(component: Component):
    # Check that all inports have data
    if not component.has_data(inports=inports):  # We do not require "Strict"
        return

    # source the data from the inports
    array: base.MdDouble = component.get_data(inports[0])
    shape: base.MdInt = component.get_data(inports[1])

    if component.debug:
        component.log(
            log_level=LogLevel.DEBUG,
            message=f"Reshaping\n{array.get_array()}\nto a shape of\n{shape.values}",
        )
    if len(shape.shape) != 1:  # Assert that the shape is only 1 dimensional, e.g. 2x2x3x1 is [2, 2, 3, 1]
        component.log(
            LogLevel.ERROR,
            message="You can only use a 1 Dimensional integer array to define the shape of a number array!",
        )
        return

    strict: bool = component.get_data("strict").value if component.has_data("strict") else False
    np_array: np.array = array.get_array()
    if strict:  # If you cannot reshape in to this new shape then raise an exception
        try:
            np_array.reshape(shape.values)
        except ValueError:
            component.log(
                LogLevel.ERROR,
                message=f"You cannot reshape an array of {np_array.size} into a shape {shape.values}!",
            )
            return

    else:  # Populate with zeros to match desired size
        np_array.resize(shape.values)

    array_msg = base.MdDouble()
    array_msg.set_array(np_array)

    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Produced:\n{np_array}")
    # send the result message to the outports (as multi_connection)
    component.send_data(array_msg, outports[0])
