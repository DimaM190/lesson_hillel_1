import string

has_htag = input("Enter expression: ")

has_htag1 = has_htag.title()

del_pun = ""
for elm in has_htag1:
    if elm not in string.punctuation and elm != " ":
        del_pun = del_pun + elm


print("#" + del_pun[0:140])
pass
