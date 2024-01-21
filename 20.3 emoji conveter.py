message=input(">")
#Good Morning :) break it in three parts
word=message.split(' ')
emojis={
    ":)":"😊",
    ":(":"😞"

}
output=""
for words in word:
    output+= emojis.get(words,words) + "  "
print(output)