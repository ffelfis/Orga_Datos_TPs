import numpy as np
import string
import re

# Función para limpiar el texto de los mensajes.

def clean_text(text):
    # Se quitan los números.
    text = re.sub('\w*\d\w*', '', text)
    # Se convierte el texto a minúsculas.
    text = text.lower()
    # Se quitan los números.
    text = re.sub('\w*\d\w*', '', text)
    # Se quitan las llaves y atributos de html.
    text = re.sub(r'<.*?>', '', text)
    # Se quitan los saltos de línea.
    text = re.sub('\n', ' ', text)
    # Se eliminan las referencias a usuarios '@user'.
    text = re.sub('@\S*', '', text)
    # Se quitan vínculos URL.
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    # Se simplifican múltiples espacios a uno solo.
    text = re.sub('(\ ){2,7}', ' ',text)
    # Se quitan los signos de puntuación.
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    # Se quitan los caracteres no ASCII
    text = re.sub(r'[^\x00-\x7F]+','ñ', text)
    return text
