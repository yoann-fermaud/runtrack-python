# --| 1 |-- #
# Loading the lowercase alphabet to a list
import string

alphabet = list(string.ascii_lowercase)
alphabet.sort(reverse=True)
print(alphabet)


# Returns: ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
# 'e', 'd', 'c', 'b', 'a']


# --| 2 |-- #
def print_reverse():
    alphabet_reverse = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_reverse.sort(reverse=True)
    print(alphabet_reverse)


print_reverse()


# --| 3 |-- #
class Alphabet:
    def __init__(self, letter: str):
        self.letter = letter

    def __reversed__(self):
        return self.letter[::-1]


instance_alphabet = Alphabet(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
     't', 'u', 'v', 'w', 'x', 'y', 'z'])

print(reversed(instance_alphabet))
