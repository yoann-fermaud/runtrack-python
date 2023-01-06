def shift_message(message, shift):
    shifted_chars = []
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code += shift
            # If the character is outside the range of lower case letters,
            # shift it around to the opposite end of the alphabet
            if char.islower():
                #  Shifts the ASCII code from 122 (letter "z") to 97 (letter "a")
                if char_code > ord("z"):
                    char_code -= 26
                #  Shifts the ASCII code from 97 (letter "a") to 122 (letter "z")
                elif char_code < ord("a"):
                    char_code += 26
            # If the character is outside the range of upper case letters,
            # shift it around to the opposite end of the alphabet
            else:
                #  Shifts the ASCII code from 90 (letter "Z") to 65 (letter "A")
                if char_code > ord("Z"):
                    char_code -= 26
                #  Shifts the ASCII code from 65 (letter "A") to 90 (letter "Z")
                elif char_code < ord("A"):
                    char_code += 26
            shifted_chars.append(chr(char_code))
        else:
            shifted_chars.append(char)

    return "".join(shifted_chars)


print(ord("a"), ord("z"))
print(ord("A"), ord("Z"))
print(shift_message("Shifted alphabet !", 3))
