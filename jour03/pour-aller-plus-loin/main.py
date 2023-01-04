class Char:
    def __init__(self, name):
        self.name = name

    def __reversed__(self):
        return self.name[::-1]


instance_char = Char("nikana")

print(f'Before reverse : {instance_char.name}')
print(f'After reverse  : {reversed(instance_char)}')

