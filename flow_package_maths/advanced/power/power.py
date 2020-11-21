from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
value = Inport(id="value", types=unions.Number, multi_connection=False)
exponent = Inport(id="exponent", types=unions.Number, multi_connection=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[value, exponent], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val: float = cast(base.Double, component.get_data(value)).value
    exp: float = cast(base.Double, component.get_data(exponent)).value

    # check for complex numbers
    if val < 0 and not exp.is_integer():
        component.log(
            log_level=LogLevel.ERROR,
            message=f"Value is negative ({val}) and the exponent is less than 1 ({exp}) "
            + "which results in a complex number. Complex numbers are not supported yet.",
        )
        return

    # power
    res = val ** exp

    # logs
    # component.log(log_level=LogLevel.DEBUG, message=f"{val} to the power of {exp} gives {res}.")

    # send message to outports
    component.send_data(base.Double(res), result)
