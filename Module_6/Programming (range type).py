words = []

while True:
    word = input("Enter a word >")
    if word.lower() == "stop":
        break
    words.append(word)

print(words)

for i in range(len(words)):
    if i % 2 == 0:
        words[i] = i * len(words[i])

print(words)
