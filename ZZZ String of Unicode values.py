
character = 'ী' #Must be one character for multi char use for loop
unicode_value_int = ord(character)
unicode_format = f"U+{unicode_value_int:04X}"

print(f"The {character} First int value {unicode_value_int} & Unicode Value is {unicode_format}")



unicode_values = [0x0041, 0x4E2D, 0x262F, 0x1DAB]  # Replace with your Unicode values

for value in unicode_values:
    character = chr(value)
    print(f"The character for Unicode value U+{value:04X} is '{character}'")

print(chr(0x23d1))





