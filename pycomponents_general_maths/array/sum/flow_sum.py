from flow import run, print, Component
from flow_types import base
import numpy as np

inports = ["values"]
outports = ["result"]

definition = {
    "name": "sum",
    "description": "Get the sum of an entire Array of Numbers.",
    "inports": [{"name": inports[0], "description": "The first number", "types": [base.MdDouble],},],
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

    # We are using numpy's built in functions so we don't have to worry
    result: float = np.sum(array)

    if component.debug is True:
        print("The sum of {0} is {1} ".format(array_msg, result))

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(result), outports[0])


if __name__ == "__main__":
    run(definition, process)
