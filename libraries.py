from my_math_functions import add_numbers
from pprint import pprint as pp
import os


print(add_numbers(5, 4))


my_dict = {num: num*num for num in range(30)}
pp(my_dict)

my_folder = os.getcwd()

print(f"Here are the files in: {my_folder}")

with os.scandir(my_folder) as folder:
    for entry in folder:
        print(entry.name)