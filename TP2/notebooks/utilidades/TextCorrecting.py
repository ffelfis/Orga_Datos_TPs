from spellchecker import SpellChecker

corrector = SpellChecker()

# Las words deben estar en minúscula para que funcione
def correct_text(text):
    word_list = text.split()
    corrected = []
    to_correct = corrector.unknown(word_list)
    
    for word in word_list:
        if word in to_correct:
            corrected.append(corrector.correction(word))
        else:
            corrected.append(word)
    return " ".join(corrected)
