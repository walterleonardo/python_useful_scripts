def replace_string(string):
    if len(string) <= 1:
        return string

    if string[:2] == "aa":
        string = "b" + replace_string(string[2:])
    elif string[:2] == "bb":
        string = "c" + replace_string(string[2:])
    else:
        string = string[0] + replace_string(string[1:])

    return string

# Example usage
input_string = "aaaaaaaa"
output_string = replace_string(input_string)
print(output_string)