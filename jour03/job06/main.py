# --| 1 |-- #
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z'] * 10

list_i = 1

while list_i < len(alphabet):
    print(alphabet[:list_i])      # We display the first character of the list
    alphabet = alphabet[list_i:]  # Allows to keep the characters of the list which are not yet displayed
    list_i += 1


# --| 2 |-- #
class Alphabet:
    def __init__(self, letter):
        self.letter = letter


instance_alphabet = Alphabet(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
     't', 'u', 'v', 'w', 'x', 'y', 'z'] * 10)

list_j = 1

while list_j < len(instance_alphabet.letter):
    print(instance_alphabet.letter[:list_j])                      # We display the first character of the list
    instance_alphabet.letter = instance_alphabet.letter[list_j:]  # Allows to keep the characters of the list which are not yet displayed
    list_j += 1
