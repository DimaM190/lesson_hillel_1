def correct_sentence(text: str) -> str:
    text_tit = text[0].title() + text[1:]
    if text_tit[-1] == ".":
        return text_tit
    return f"{text_tit}."


print(correct_sentence("Greetings. Friends"))

assert correct_sentence("greetings, friends") == "Greetings, friends.", "Test1"
assert correct_sentence("hello") == "Hello.", "Test2"
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", "Test3"
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", "Test4"
assert correct_sentence("greetings, friends.") == "Greetings, friends.", "Test5"
print("ОК")
