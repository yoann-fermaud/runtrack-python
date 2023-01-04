# --| 1 |-- #
def my_print_name(name: str):
    print(f'{name}')


my_print_name('Yoann')
my_print_name('Zoé')


# --| 2 |-- #
def my_print_name_other(name_other: str) -> str:  # Type return (str)
    return name_other


print(my_print_name_other('Yoann'))
print(my_print_name_other('Zoé'))
