def sentence_maker(phrase):
    interrogatives = ("how", "why", "what")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Sey something: ")
    if user_input == '\end':
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))

# print(sentence_maker("how are you"))
# print(sentence_maker("hello!")) 