import pandas as pd
import openpyxl

df = pd.read_excel("Zach Chart Only.xlsx")
print(df)

# Task 1
class1 = input("Enter a class to list all names.")
students_class1_df = df.dropna(subset=[class1])[class1]
all_students_class1 = []
for student in students_class1_df:
    all_students_class1.append(student)
print(all_students_class1)

# Task 2
classes2 = input("Enter classes separated by commas to find all similar students.").split(',')
classes2_stripped = [classe2.strip() for classe2 in classes2]
filtered_df = df.loc[:, classes2_stripped]

value = None
for col in filtered_df.columns:
    if value is None:
        value = set(filtered_df[col])
    else:
        value = value.intersection(set(filtered_df[col]))
    if not value:
        break

nonempty_students = pd.Series(list(value)).dropna()
print(list(nonempty_students))


# Task 3
student3 = input("Enter a student to list all column types.")
cols_with_value = list(df.columns[df.isin([student3]).any()])
print(cols_with_value)
