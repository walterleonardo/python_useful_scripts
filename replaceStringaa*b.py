import re

def replace_double_letters(quantity):
    string = 'a' * quantity
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = string

    for i in range(len(alphabet)-1):
        pattern = alphabet[i]*2
        replacement = alphabet[i+1]

        new_string = re.sub(pattern, replacement, new_string)

    return new_string

# Ejemplo de uso
quantity = 67108876
result = replace_double_letters(quantity)
print(result)