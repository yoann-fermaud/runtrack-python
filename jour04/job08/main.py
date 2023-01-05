L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

pair = 0

for i in range(len(L)):
    if L[i] % 2 == 0:
        pair += 1

print(f'Even number : {pair}')
