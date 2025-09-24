people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

mx = people[0]
for item in people:
    if item[1] > mx[1]:
        mx = item
print(mx)