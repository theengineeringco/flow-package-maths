from flow import run, print, Component
from flow_types import base
from flow_pycomponents_utils import call_function_with_data
import uuid

inports = ["values"]
outports = ["result"]

definition = {
    "name": "mass_sum",
    "description": "Sum an entire array at the inport",
    "inports": [
        {
            "name": inports[0],
            "description": "The array of numbers",
            "types": [base.Double, base.Int],
            "addressable": True,
        }
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": [base.Double]}],
}


# The actual numeric function we are performing
def adding_function(use_values: dict = None):
    if use_values is None:
        use_values = {"uuid": 1, "uuid": 2.5}
    return_value = 0
    for each in use_values.values():
        return_value += each
    return return_value


# The process that the component performs
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data_addressable(inports[0]):
        raise ValueError("No data found in port {0}".format(inports[0]))

    get_data_arr = {}
    for each in component.get_data_addressable(inports[0]):
        get_data_arr[uuid.uuid1()] = each

    # actually run the adding function with the inputs. You can write the function explicitly instead but
    # we leverage the "call_function_with_data" as it works well for maths functions
    use_values, the_result = call_function_with_data(get_data_arr, adding_function)

    if component.debug is True:
        print("{0} is {1}".format(inports, use_values))
        print("The Result of adding these is {0} ".format(the_result))

    # There is only one message from this output
    component.send_data_addressable(base.Double(the_result), outports[0])


if __name__ == "__main__":
    run(definition, process)
