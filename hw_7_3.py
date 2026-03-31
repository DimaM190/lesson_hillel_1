def second_index(text: str, some_str: str):
    count_index = text.count(some_str)
    if count_index < 2:
        return None
    first_index = text.index(some_str)
    second_index = text.index(some_str, first_index + 1)
    return second_index


result = second_index("sims", "s")

assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"
print("ОК")
