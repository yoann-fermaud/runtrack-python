char = input(f'Type a sentence : ')
print(char)

if 'e' in char.lower():
    count_e = char.lower().count('e')

    if count_e > 1:
        print(f'There are {count_e} "e" in your sentence.')
    else:
        print(f'There is {count_e} "e" in your sentence.')

else:
    print(f'There is no "e".')
