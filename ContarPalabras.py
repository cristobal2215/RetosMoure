def ContarPalabras(text):
    words = text.split()
    palabras = []
    for word in words:
        ajuste_palabra = word.strip().lower().replace(',','')
        palabras.append(ajuste_palabra)
    word_count = {}
    for word in palabras:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

print(ContarPalabras('hola hola, Hola, Hola'))