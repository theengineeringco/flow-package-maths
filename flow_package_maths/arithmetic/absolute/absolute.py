from flow import Ports, Process
from flow.testing import ComponentTest
from flow_types import base

# Define ports
ports = Ports()

# Add inports
ports.add_inport(id="value", types=[base.Double, base.Int])

# Add outports
ports.add_outport(id="result", types=[base.Double])


# Process
def process(component: Process):

    # Check all connected inports have data
    if not component.has_data():
        return

    # Get the data from each import
    value: float = component.get_data("value").value

    # Component Content
    out_val = abs(value)

    # Pack the produced data into messages that will be sent from each outport
    result_msg = base.Double(out_val)

    # Send the data from each outport
    component.send_data(result_msg, "result")


# Test
if __name__ == "__main__":

    inports_data = {
        "value": base.Double(-1.0),
    }

    outport_value = ComponentTest(__file__).run(inports_data)
    assert outport_value["result"] == base.Double(1.0)
    print(outport_value["result"])
