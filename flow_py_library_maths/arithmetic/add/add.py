from flow import Component, Definition, Inport, LogLevel, Outport
from flow_types import base, unions

# ports
v1 = Inport(id="v1", types=[unions.Number], multi_connection=False)
v2 = Inport(id="v2", types=[unions.Number], multi_connection=False)
result = Outport(id="result", types=[unions.Number])

# comp definition
definition = Definition([v1, v2], [result])


def process(component: Component):

    if not component.has_data():
        return

    # get inports data
    val1: base.Double = component.get_data(v1).value
    val2: base.Double = component.get_data(v2).value

    # add
    res = val1 + val2

    # output message
    res_msg = base.Double(res)

    # logs
    component.log(log_level=LogLevel.DEBUG, message=f"Adding {val1} to {val2} gives {res}.")

    # send message to outports
    component.send_data(res_msg, result)
