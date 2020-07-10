import numpy as np
from flow import Component, print, run
from flow_types import base

inports = ["values"]
outports = ["result"]

definition = {
    "name": "average",
    "description": "Get the average of an entire Array of Numbers.",
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
    array: np.array = array_msg.get_array()

    # We are using numpy's built in functions so we don't have to worry
    result: float = np.mean(array)

    if component.debug is True:
        print(f"The average of {array_msg} is {result} ")

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(result), outports[0])


if __name__ == "__main__":
    run(definition, process)
