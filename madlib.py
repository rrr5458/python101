name = input("Pick a name: ")
noun1 = input("Pick a noun ")
noun2 = input("Pick a noun ")
adjective1 = input("Pick an adjective ")
adjective2 = input("Pick an adjective ")
adjective3 = input("Pick an adjective ")
verb1 = input("Pick verb ")
verb2 = input("Pick verb ")
verb3 = input("Pick verb ")

sentence = "When " + name + " was younger, he was a " + noun1 + ". Over the years, he grew into a human. When he was a " + noun1 + " he liked to " + verb1 + ". It would make his " + noun2 + " " + adjective1 + ". " + adjective2 + " " + noun1 + "s are the worlds best at " + verb2 + "ing. Right before they turn into a human, they " + verb3 + " a  blade of "  + adjective3 + " grass."
print(sentence)
sentence_list = []
for letter in sentence:
    sentence_list.append(letter)
print(len(sentence_list))