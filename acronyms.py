user_input = str(input("Enter a Phrase: "))
text = user_input.split()
result = ""
for words in text:
    result += str(words[0].upper())
print(result)

