students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]
count = 0
for student in students:
    if 'Matematika' in student[1]:
        count += 1
print(count)