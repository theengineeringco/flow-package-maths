from math import ceil, floor
from typing import Any, Dict, List

from flow import Ports, Process, Settings, Setup
from flow.definitions.settings.setting import Option
from flow.testing import ComponentTest
from flow_types import base
from flow_types.typing import FlowType

up_name = "up"
down_name = "down"
nearest_name = "nearest"

round_types: List[Option] = [
    Option(up_name, "Round Up"),
    Option(down_name, "Round Down"),
    Option(nearest_name, "Round to Nearest"),
]

settings = Settings()
settings.add_select_setting(id="round_type", options=round_types, default=nearest_name)

ports = Ports()
ports.add_inport(id="value", types=[base.Double, base.Int, base.Bool])
ports.add_inport(id="decimal_places", types=[base.Int, base.Bool], default=base.Int(0))
ports.add_outport(id="result", types=[base.Double])


def setup(component: Setup):

    round_type = str(component.get_setting("round_type"))
    component.set_variable("round_type", round_type)


def process(component: Process):

    round_type = component.get_variable("round_type")

    value = float(component.get_data("value"))
    decimal_places = int(component.get_data("decimal_places"))

    multiplier = 10 ** decimal_places

    # round
    if round_type == nearest_name:
        intermediate = round(value, decimal_places)
    elif round_type == up_name:
        intermediate = ceil(value * multiplier) / multiplier
    elif round_type == down_name:
        intermediate = floor(value * multiplier) / multiplier

    if decimal_places <= 0:
        result: Any = int(intermediate)
    else:
        result = intermediate

    # send message to outports
    component.send_data(base.Double(result), "result")


if __name__ == "__main__":
    setting_data = {
        "round_type": nearest_name,
    }

    inports_data: Dict[str, FlowType] = {
        "value": base.Double(567.4354),  # noqa: WPS432
        "decimal_places": base.Int(1),
    }

    outport_value = ComponentTest(__file__).run(inports_data, setting_data)
    print(outport_value["result"])
