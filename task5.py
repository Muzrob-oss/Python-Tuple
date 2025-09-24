numbers = (3, 6, 7, 8, 10, 11)

son = []
for number in numbers:
    if number % 2 == 0:
        son += (number,)
print(son)