def remove_chars(chars,phrase):
    string_sans_chars = ""
    for letter in phrase:
        if letter not in chars:
            string_sans_chars += letter
    return string_sans_chars

print(remove_chars("aeiou","Hello World"))

def remove_list_els(chars,phrase):
    string_sans_chars = []
    for letter in phrase:
        if letter not in chars:
            string_sans_chars += letter
    return string_sans_chars

print(remove_list_els(list("aeiou"),list("Hello World")))

