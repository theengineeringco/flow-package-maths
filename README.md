# flow_py_library_general_maths

[![python-version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Package of Python Flow Components

## Components

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
flow library add --type python git+https://github.com/theengineeringco/flow_py_library_general_maths.git
```

## Example code implementation

A typical Basic Maths component is made up of 3 things:

1. Port Definitions
2. Flow Component Definition
3. Flow Process (as a function)

The port definitions are typically handled as arrays to allow the UI, the component, and the testing to access the names easily. _In many other component libraries the inports and outports are expressed as dicts to allow a name and a type to be assigned. All Basic Maths components allow for Ints and Doubles as inputs (or in the case of inherent Array functions, such as Mass_Sum, we allow MdInts and MdDoubles)._

```python
inports = ["val1", "val2"]
outports = ["result"]
```

The Flow Definition is used by Flow: backend for types and port handling; front-end for Name, Description, and any other functionality we might add (such as Icons, Web-links, Viewport definitions).

```python
allowable_types = unions.Number  # This is a union of base.Int and base.Double
definition = {
    "name": "divide",
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
    "outports": [
        {
            "name": outports[0],
            "description": "The result number",
            "types": allowable_types,
        }
    ],
}
```

The Flow Process for the component is pretty easy to implement as we simply call the mathematical directly with the component port data.

```python
def process(component: Component):
    # check that the components have data --> this can be modified if you want to set explicit defaults etc.
    if not component.has_data():
        return

    # source the data from the inports
    value1_msg: base.Double = component.get_data(inports[0])
    value2_msg: base.Double = component.get_data(inports[1])

    val1 = value1_msg.value
    val2 = value2_msg.value
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"Dividing {val1} by {val2}")

    # calculate the result
    result = val1 / val2
    result_msg = base.Double(result)
    if component.debug:
        component.log(log_level=LogLevel.DEBUG, message=f"The result is {result}.")

    # send the result message to the outports (as multi_connection)
    component.send_data(result_msg, outports[0])
```

## License

[MIT](https://github.com/theengineeringco/flow_py_library_general_maths/blob/master/LICENSE)

## Credits

This package was created with [theengineeringco/FlowPythonCookiecutter](https://github.com/theengineeringco/FlowPythonCookiecutter).
