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


def send_email(recipient: str, email_body) -> None:
    print(f"sending emeil to {recipient}...".format(recipient))


def validate_not_hashable(value) -> None:
    hash(value)


def send_email_manager() -> None:
    manager_mail = "example@ukr.net"
    text = "rgetgetg"
    send_email(manager_mail, text)
