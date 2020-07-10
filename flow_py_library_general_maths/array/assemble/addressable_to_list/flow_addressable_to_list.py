from typing import List

import numpy as np
from flow import Component, print, run
from flow_types import base

inports = ["values"]
outports = ["array"]

definition = {
    "name": "addressable_to_list",
    "description": "Assemble the input values in to a list in the order with which they were recieved.",
    "inports": [
        {"name": inports[0], "description": "All of the numbers", "types": [base.Double], "addressable": True},
    ],  # TODO these will also be used for MdArrays. Need a consistent way, or do we have specific versions?
    "outports": [{"name": outports[0], "description": "The resulting array (list)", "types": [base.MdDouble]}],
    # We enforce doubles for maths
}


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data_addressable(inports[0]):
        return

    # source the data from the inports
    addr_lst: List[float] = component.get_data_addressable(inports[0])
    addr_lst = [
        idx_msg.value for idx_msg in addr_lst
    ]  # They come in as a list of FlowMessages, need to extract their numbers!

    array_msg = base.MdDouble()
    array_msg.set_array(np.array(addr_lst))  # Np List implementation automatically

    print(f"Compiling the list of {addr_lst} in to an MdDouble of length {len(array_msg.values)} (1 dimensional).")

    # send the result message to the outports (as addressable)
    component.send_data_addressable(array_msg, outports[0])


if __name__ == "__main__":
    run(definition, process)
