from typing import List

import numpy as np
from flow import Component, LogLevel
from flow_types import base

inports = ["array", "index_coord"]
outports = ["result_array"]

definition = {
    "name": "item_by_coord_index",
    "description": "Get an item from an MdDouble array by coordinate indices (MdInt).",
    "inports": [
        {"name": inports[0], "description": "The array", "types": [base.MdDouble]},
        {
            "name": inports[1],
            "description": "The coordinates of the item",
            "types": [base.MdInt],
        },  # base.MdArray(ints)?
    ],  # TODO these will also be used for MdArrays. Need a consistent way, or do we have specific versions?
    "outports": [{"name": outports[0], "description": "The retrieved value", "types": [base.Double]}],
    # We enforce doubles for maths
}


# The process that the component performs
def process(component: Component):
    # Check that all inports have data
    if not component.has_data():
        return

    # source the data from the inports
    array: base.MdDouble = component.get_data(inports[0])
    index: base.MdInt = component.get_data(inports[1])

    if len(index.shape) != 1:  # Assert that the coordinates are only 1 dimensional, e.g. [2, 2, 3, 1]
        component.log(
            LogLevel.ERROR,
            message=(
                "You can only use a 1 Dimensional integer array to retrieve a coordinate value from a number array!",
            ),
        )

        return

    index_coords: List[int] = index.values
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Retrieving the {index_coords}th...")

    np_array: np.array = array.get_array()
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"...from the array {np_array}")

    return_value: float = np_array[tuple(index_coords)]

    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Retrieved:\n{return_value}")
    # send the result message to the outports (as multi_connection)
    component.send_data(base.Double(return_value), outports[0])
