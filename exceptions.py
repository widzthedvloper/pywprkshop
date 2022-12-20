try:
    int("q")
except ValueError:
    print("This is not a valide int")

my_dict = {1: 1}

user_input = 2

try:
    int(user_input)
    my_dict[user_input]
except (ValueError, KeyError):
    print("Sorry, an error occur")

