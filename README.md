# pycomponents_general_maths

[![python-version](https://img.shields.io/badge/python-3.6%2B-blue)]()
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Package of Python Flow Components

## Components
These components depend on the pycomponents_utils library and not on anything else.

This library includes General Mathematical components, such as Arithmetic (Plus, Multiply etc.), Logarithmic and Exponential (such as Ln, e^n, power(a, b)), and Trigonometric (sin, cos, tan etc.).

## Features
Components can recieve either a single value on each input or an array of values to which the mathematical function will be applied to each value in the array individually.

You may allow either 1 value on each port, exactly N values on any number of ports (including all inports).
Having N, M number of values on port1, port2 will result in failure as how do we interpret that consistently?

## Making your own new mathematical components
It is entirely possible to make new components using the FlowPythonCookieCutter, however there is functionality in the Pycomponents Utils that enables the Array Maths to be applied, and to minimise code-count for the user.

A faster practice is to copy the "divide" folder and work from there. `flow_divide.py` is the component definition and process. `test_divide.py` is where the component testing functions are stored.

## Installation

```bash
flow library add --type python git+https://github.com/theengineeringco/pycomponents_general_maths.git
```
## Example code implementation
A typical Basic Maths component is made up of 4 things:
1. Port Definitions
2. Flow Component Definition
3. Mathematical Equation (as a function)
4. Flow Process (as a function) 

The port definitions are typically handled as arrays to allow the UI, the component, and the testing to access the names easily. *In many other component libraries the inports and outports are expressed as dicts to allow a name and a type to be assigned. All Basic Maths components allow for Ints and Doubles (and Arrays of each) as inputs only, with only very few exceptions.* 

```python
inports = ["val1", "val2"]
outports = ["result"]
```

The Flow Definition is used by Flow: backend for types and port handling; front-end for Name, Description, and any other functionality we might add (such as Icons, Web-links, Viewport definitions).

```python
allowable_types = ["base.Int", "[]base.Int", "base.Double", "[]base.Double"]
definition = {
    "name": "Divide",
    "description": "Divides the first number by the second number.",
    "inports": [
        {
            "name": inports[0],
            "description": "The first number",
            "types": allowable_types,
        },
        {
            "name": inports[1],
            "description": "The second number",
            "types": allowable_types,
        },
    ],
    "outports": [{"name": outports[0], "description": "The result number", "types": allowable_types}],
}
```

The reason we have the mathematical function separate from the `process` function is so that it can behave agnostically to arrays or single-value calls. i.e. The The mathematical function is written only for single value group inputs, and it is the `call_function_with_data` method from Pycomponents_Utils that handes the array-ness of inports.

```python
# The actual numeric function we are performing
def dividing_function(use_values: dict = {"val1": 1, "val2": 2.5}):
    the_values = list(use_values.values())
    return_value = the_values[0]
    for idx in range(1, len(the_values)):
        return_value /= the_values[idx]
    return return_value
````

Finally, the Flow Process for the componet is pretty easy to implement as a lot of the complexity is handled by the Pycomponents Utils functions.
It is the `call_function_with_data` method from PyComponents Utils that handles a lot of the checking and packaging of data in to the `dividing_function` function.

```python
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not (component.has_data(inports[0]) and component.has_data(inports[1])):
        return

    # source the data from the inports
    data1 = component.get_data(inports[0])
    data2 = component.get_data(inports[1])

    get_data_arr = {inports[0]: data1, inports[1]: data2}
    # actually run the dividing function with the inputs. You can write the function explicitly instead but
    # we leverage the "call_function_with_data" as it works well for maths functions
    use_values, the_result = call_function_with_data(get_data_arr, dividing_function)

    if component.debug is True:
        print("{0} is {1}".format(inports, use_values))
        print("The Result of dividing A by B is {0} ".format(the_result))

    # send either a single message or an array of messages depending on how many inputs/outputs you make
    if isinstance(the_result, list):  # TODO: want to be able to remove this
        msgs = []
        for each_result in the_result:
            msgs.append(base.Double(each_result))
        component.send_data(msgs, outports[0])
    else:
        component.send_data(base.Double(the_result), outports[0])
```

*n.b. that sections of the process code are likely to be removed as the send_data method becomes more scalable and the debugging process becomes more standardised.*

## License

[MIT](https://github.com/theengineeringco/pycomponents_general_maths/blob/master/LICENSE)

## Credits

This package was created with [theengineeringco/FlowPythonCookiecutter](https://github.com/theengineeringco/FlowPythonCookiecutter).
