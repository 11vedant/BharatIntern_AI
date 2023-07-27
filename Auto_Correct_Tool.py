from spello.model import SpellCorrectionModel

model = SpellCorrectionModel(language="en")

with open ("words.txt") as file:

    data = file.readlines()

    model.train(data)
    model.save("")

    model.load("model.pkl")

lines = input("Enter the sentence/word : ")
words = lines.split()

correct_words = []
for word in words:
    corrected = model.spell_correct(word)
    correct_words.append(corrected['spell_corrected_text'])
    
corrected_sentence = " ".join(correct_words)
print("Corrected Sentence : ",corrected_sentence)