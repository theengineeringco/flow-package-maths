from typing import cast

from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
value1 = Inport(id="value1", types=unions.Number, multi_connection=False)
value2 = Inport(id="value2", types=unions.Number, multi_connection=False)
result = Outport(id="result", types=unions.Number)

# comp definition
definition = Definition(inports=[value1, value2], outports=[result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val1: float = cast(base.Double, component.get_data(value1)).value
    val2: float = cast(base.Double, component.get_data(value2)).value

    # add
    res = val1 + val2

    # output message
    result_msg = base.Double(res)

    # logs
    # component.log(log_level=LogLevel.DEBUG, message=f"Adding {val1} to {val2} gives {res}.")

    # send message to outports
    component.send_data(result_msg, result)

    # TODO: include support for different types for all maths components
    # try:
    #     flow_type_val1: base.BaseType = deserialise.get_serialised_message_type(value1)
    #     flow_type_val2: base.BaseType = deserialise.get_serialised_message_type(value2)
    # except TypeError:
    #     component.log(log_level=LogLevel.ERROR, message="Invalid values.")
    #     return

    # if flow_type_val1 == base.Int and flow_type_val2 == base.Int:
    #     # get inports data
    #     val1_int: int = cast(base.Int, component.get_data(value1)).value
    #     val2_int: int = cast(base.Int, component.get_data(value2)).value

    #     res = val1_int + val2_int
    #     result_msg = base.Int(res)
    # else:
    #     # get inports data
    #     val1_float: float = cast(base.Double, component.get_data(value1)).value
    #     val2_float: float = cast(base.Double, component.get_data(value2)).value

    #     res = val1_float + val2_float
    #     result_msg = base.Double(res)
