message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "🙂",
    ":(": "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
output = output[:len(output) - 1]
print(output)
