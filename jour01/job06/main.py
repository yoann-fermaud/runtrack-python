class MaString:
    ma_string = "je suis une String"

    def __init__(self, ma_string: str):
        self.ma_string = ma_string


new_string = MaString("je suis une nouvelle String")

print(MaString.ma_string)
print(new_string.ma_string)
