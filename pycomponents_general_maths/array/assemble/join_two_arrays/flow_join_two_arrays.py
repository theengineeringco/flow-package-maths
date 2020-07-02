from typing import List

import numpy as np
from flow import Component, print, run
from flow_types import base

inports = ["array_1", "array_2"]
outports = ["result_array"]

definition = {
    "name": "join_two_arrays",
    "description": "Join two arrays of equal dimensions in to a single array.",
    "inports": [
        {"name": inports[0], "description": "The first array", "types": [base.MdDouble]},
        {"name": inports[1], "description": "The second array", "types": [base.MdDouble]},
        {
            "name": "vertical",
            "description": "Default the concatination vertically?",
            "types": [base.Bool],
            "required": False,
        },
    ],  # TODO these will also be used for MdArrays. Need a consistent way, or do we have specific versions?
    "outports": [{"name": outports[0], "description": "The joined array", "types": [base.MdDouble]}],
    # We enforce doubles for maths
}


# The process that the component performs
def process(component: Component):
    # Check that all inports have data
    if not all([component.has_data(idx) for idx in inports]):
        return

    # source the data from the inports
    vals = []
    for ndx in (0, 1):
        array: base.MdDouble = component.get_data(inports[ndx])
        vals.append(array.get_array())

    array_msg = base.MdDouble()

    vertical: bool = component.get_data("vertical").value if component.has_data("vertical") else True
    if vertical:
        array_msg.set_array(np.vstack(tuple(vals)))  # Np List implementation automatically
    else:  # Populate horizontally
        array_msg.set_array(np.hstack(tuple(vals)))

    print("Joining\n{0}\nwith\n{1}\n{2}ly.".format(vals[0], vals[1], ("vertical" if vertical else "horizontal")))
    print("Produced:\n{0}".format(array_msg.get_array()))
    # send the result message to the outports (as addressable)
    component.send_data_addressable(array_msg, outports[0])


if __name__ == "__main__":
    run(definition, process)