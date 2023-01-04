def remove_special_characters(string):
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    new_string = ""
    for character in string:
        if character in allowed_characters:
            new_string += character
    return new_string

def capitalize_words(string, should_remove_special_characters=False):
    if should_remove_special_characters:
        string = remove_special_characters(string)

    words = string.split()
    capitalized_words = []
    for word in words:
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)
    return " ".join(capitalized_words)

string = "hOLA, MUNDO!"
capitalized_string = capitalize_words(string, should_remove_special_characters=True)
print(capitalized_string)