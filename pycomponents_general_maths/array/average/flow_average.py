from flow import run, print, Component
from flow_types import base
from flow_pycomponents_utils import call_function_with_data

inports = ["values"]
outports = ["result"]

definition = {
    "name": "average",
    "description": "Get the average of an entire Array of Numbers.",
    "inports": [{"name": inports[0], "description": "The first number", "types": [base.MdDouble],},],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}

# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data(inports[0]):
        return

    # source the data from the inports
    values = component.get_data(inports[0])

    result: float = sum(values.values) / len(
        values.values
    )  # MdDoubles and MdInts both have all values stored as a list anyway!

    if component.debug is True:
        print("{0} is {1}".format(inports, values))
        print("The Result of dividing A by B is {0} ".format(result))

    # send the result message to the outports (as addressable)
    component.send_data_addressable(base.Double(result), outports[0])


if __name__ == "__main__":
    run(definition, process)
