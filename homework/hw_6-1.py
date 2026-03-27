import string

user_let = input("Enter two letters separated by a hyphen: ")
user_let1 = list(user_let)
al_bet = list(string.ascii_letters)
index1 = al_bet.index(user_let1[0])
index2 = al_bet.index(user_let1[-1])
print(string.ascii_letters[index1 : index2 + 1])

pass
