from flow.test_framework.helpers import strip_test_data_unique_info


def basic_test_eval(test_data: dict, tolerance: float = 1e-6, type_test: bool = True, normalise: bool = True) -> bool:
    """
        Test a component in the standard fashion.

        test_data: The resulting test_data from component.test(inputs, outputs)
        tolerance (optional): the tolerance to check for
        type_test (optional): assert types are the same, too
        ---------------------------------

        usage:
            def run_test_func(inputs, outputs, flow: FlowTest):
                global component_file
    test_data = flow.test(component_file, inputs, outputs)
                basic_test_eval(test_data)
        ----------------------------------

        returns a bool True by default
    """
    for port_data in test_data.values():
        for p_exp, p_got in zip(port_data.expected, port_data.got):
            if normalise:  # Strip the info fields (these will never match in normal tests)
                p_exp = strip_test_data_unique_info(p_exp)
                p_got = strip_test_data_unique_info(p_got)
            if isinstance(p_exp, list):
                for idx, _ in enumerate(p_exp):
                    assert p_exp[idx] == p_got[idx]  # noqa: S101 - Allow Assert
            else:
                assert p_exp == p_got  # noqa: S101 - Allow Assert
    return True
