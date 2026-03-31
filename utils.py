def get_unique_values(some_itersble: list[str, bool, int, float] | set | str) -> set:

    unique_values = set(some_itersble)
    return unique_values


# divide two numbers, get 0 if impossible


def get_division(dividend: int, divisor: int) -> float:
    """
    we return 0 if divisor 0 because of task #64689
    """
    if not divisor:
        return 0.0
    result = dividend / divisor
    return result



