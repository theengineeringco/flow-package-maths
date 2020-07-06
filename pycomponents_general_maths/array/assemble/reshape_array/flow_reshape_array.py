from typing import List

import numpy as np
from flow import Component, print, run
from flow_types import base

inports = ["array", "shape"]
outports = ["result_array"]

definition = {
    "name": "reshape_array",
    "description": "Reshape an MdDouble array to a new shape provided as a list of integers.",
    "inports": [
        {"name": inports[0], "description": "The array", "types": [base.MdDouble]},
        {
            "name": inports[1],
            "description": "The shape as a 1D array",
            "types": [base.MdInt],
        },  # TODO base.MdArray(ints)
        {"name": "strict", "description": "Do not allow resizing.", "types": [base.Bool], "required": False},
    ],  # TODO these will also be used for MdArrays. Need a consistent way, or do we have specific versions?
    "outports": [{"name": outports[0], "description": "The reshaped array", "types": [base.MdDouble]}],
    # We enforce doubles for maths
}


# The process that the component performs
def process(component: Component):
    # Check that all inports have data
    if not all([component.has_data(idx) for idx in inports]):
        return

    # source the data from the inports
    array: base.MdDouble = component.get_data(inports[0])
    shape: base.MdInt = component.get_data(inports[1])

    assert len(shape.shape) == 1  # Assert that the shape is only 1 dimensional, e.g. 2x2x3x1 is [2, 2, 3, 1]

    strict: bool = component.get_data("strict").value if component.has_data("strict") else False
    np_array: np.array = array.get_array()
    if strict:  # If you cannot reshape in to this new shape then raise an exception
        np_array.reshape(shape.values)
    else:  # Populate with zeros to match desired size
        np_array.resize(shape.values)

    array_msg = base.MdDouble()
    array_msg.set_array(np_array)

    print("Reshaping\n{0}\nto a shape of\n{1}".format(array.get_array(), shape.values))
    print("Produced:\n{0}".format(np_array))
    # send the result message to the outports (as addressable)
    component.send_data_addressable(array_msg, outports[0])


if __name__ == "__main__":
    run(definition, process)
