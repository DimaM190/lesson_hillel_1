import string
import keyword

name_var = input("Enter name variable for checking: ")

if name_var == "":
    print(False)
    exit()
if name_var[0].isdigit():
    print(False)
    exit()
if name_var in keyword.kwlist:
    print(False)
    exit()
if name_var.count("_") > 1:
    print(False)
    exit()

for elm in name_var:
    if elm.isupper():
        print(False)
        exit()
    if elm in string.punctuation and elm != "_":
        print(False)
        exit()
    if elm == " ":
        print(False)
        exit()
print(True)
