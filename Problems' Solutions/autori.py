phrase = input()

words = phrase.split("-")

letters = [letter[0] for letter in words]
print("".join(letters))