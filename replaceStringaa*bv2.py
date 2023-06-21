def replace_double_letters(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ""

    i = 0
    while i < len(string):
        if i+1 < len(string) and string[i] == string[i+1]:
            index = alphabet.index(string[i])
            new_string += alphabet[index+1]
            i += 2
        else:
            new_string += string[i]
            i += 1

    return new_string

# Ejemplo de uso
input_string = "aaaaaaaaaaaaa"
result = replace_double_letters(input_string)
print(result)