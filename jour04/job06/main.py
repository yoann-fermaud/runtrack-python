L = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]


# --| 1 |-- #
def swap_first_last(L):
    size = len(L)
    temp = L[0]
    L[0] = L[size - 1]
    L[size - 1] = temp
    return L


print(f'Method one  : ')
print(f'Before swap : {L}')
print(f'After swap  : {swap_first_last(L)}')

# --| 2 |-- #
print(f'\nMethod two  : ')
print(f'Before swap : {L}')
L[0], L[-1] = L[-1], L[0]
print(f'After swap  : {L}')
