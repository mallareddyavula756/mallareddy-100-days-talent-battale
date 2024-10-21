def find_ascii_value(character):
    return ord(character)
char = input("Enter a character: ")
ascii_value = find_ascii_value(char)
print(f"The ASCII value of '{char}' is {ascii_value}")
