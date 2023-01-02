def texto_a_morse(texto):
  codigos_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.—.—.—',
    ',': '——..——', '?': '..——..', '/': '—..—.', '\'': '.—..—.',
  }
  
  codigo_morse = ''
  
  for caracter in texto:
    if caracter == ' ':
      codigo_morse += ' '
    else:
      codigo_morse += codigos_morse[caracter.lower()] + ' '
  
  return codigo_morse

print(texto_a_morse('Chocapic. Es una marca de cereales?'))