import utils_2


def test_process_summa():
    number_1, number_2 = [1, 2]
    expected_result = 3
    actual_result = utils_2.process_summa(number_1, number_2)
    assert expected_result == actual_result


def test_process_substraction():
    number_1, number_2 = [1, 6]
    expected_result = -5
    actual_result = utils_2.process_substraction(subtrahend=number_1, minuend=number_2)
    assert expected_result == actual_result
