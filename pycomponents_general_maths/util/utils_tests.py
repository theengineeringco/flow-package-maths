import pytest


def standard_test(test_data: dict, tolerance: float = 1e-6, type_test: bool = True) -> bool:
    """
        Standard testing of components.

        ---------------------------------

        test_data: The resulting test_data from component.test(inputs, outputs)
        tolerance (optional): the tolerance to check for
        type_test (optional): assert types are the same, too
        
        ---------------------------------

        usage:
            def run_test_func(inputs, outputs, flow: FlowTest):
                global component_file
    test_data = flow.test(component_file, inputs, outputs)
                standard_test(test_data)

        ----------------------------------

        returns a bool True by default
    """

    for port_data in test_data.values():
        for p_exp, p_got in zip(port_data.expected, port_data.got):
            if isinstance(p_exp, list):
                for i in range(0, len(p_exp)):
                    assert p_exp[i]["value"] == pytest.approx(p_got[i]["value"], rel=tolerance)
            else:
                assert p_exp["value"] == pytest.approx(p_got["value"], rel=tolerance)
    return True
