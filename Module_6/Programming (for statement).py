user_input = input("Enter some words >")

words = user_input.split()

print(words)

for word in words:
    print(f"{word} {word.upper()}")