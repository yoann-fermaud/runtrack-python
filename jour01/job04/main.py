# --| 1 |-- #
# Loading the lowercase alphabet to a list
import string

alphabet = list(string.ascii_lowercase)
print(alphabet)


# Returns: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
# 'v', 'w', 'x', 'y', 'z']


# --| 2 |-- #
def print_straight():
    alphabet_straight = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(alphabet_straight)


print_straight()


# --| 3 |-- #
class Alphabet:
    def __init__(self, letter: str):
        self.letter = letter


instance_alphabet = Alphabet(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
     't', 'u', 'v', 'w', 'x', 'y', 'z'])

print(instance_alphabet.letter)
