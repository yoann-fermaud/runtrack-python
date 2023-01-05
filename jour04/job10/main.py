L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

multiplication = 1

for i in range(len(L)):
    if 24 < L[i] < 91:
        multiplication *= L[i]

print(f'Products of the values in the intervals [25, 90] of the list L : {multiplication}')
