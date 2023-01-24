import random
import pandas

# List comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = "Georgi"
letters_list = [letter for letter in name]

list1 = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
list2 = [name for name in names if len(name) <= 4]
list3 = [name.upper() for name in names if len(name) > 5]

students_scores = {name: random.randint(1, 100) for name in names}
passed_students = {name: value for (name, value) in students_scores.items() if value >= 60}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)
