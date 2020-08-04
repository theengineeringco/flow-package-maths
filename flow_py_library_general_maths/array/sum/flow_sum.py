import numpy as np
from flow import Component, LogLevel
from flow_types import base

inports = ["values"]
outports = ["result"]

definition = {
    "name": "sum",
    "description": "Get the sum of an entire Array of Numbers.",
    "inports": [{"name": inports[0], "description": "The first number", "types": [base.MdDouble]}],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(inports[0]):
        return

    # source the data from the inports
    array_msg: base.MdDouble = component.get_data(inports[0])
    array: np.ndarray = array_msg.get_array()
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Calculating the sum of {array}")

    # We are using numpy's built in functions so we don't have to worry
    result: float = np.sum(array)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"The sum is {result}.")

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(result), outports[0])
