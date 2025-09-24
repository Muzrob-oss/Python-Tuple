orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

a = []
for order in orders:
    if order[0] % 2 == 0:
        a.append(order)
print(a)