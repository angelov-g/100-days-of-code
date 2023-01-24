# List comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = "Georgi"
letters_list = [letter for letter in name]

list1 = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
list2 = [name for name in names if len(name) <= 4]
list3 = [name.upper() for name in names if len(name) > 5]
print(list3)