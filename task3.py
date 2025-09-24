words = ("apple", "banana", "strawberry", "kiwi")
meva = ""
for w in words:
    if len(w) > len(meva):
        meva = w
print(meva)