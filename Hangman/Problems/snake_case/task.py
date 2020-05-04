word = input()
for letter in word:
    if letter.isupper():
        print("_", end="")
    print(letter.lower(), end="")
print()
