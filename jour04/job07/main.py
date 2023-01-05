L = [8, 24, 48, 2, 16]

multiple = 0

for i in range(len(L)):
    if L[i] % 3 == 0:
        multiple += 1

print(f'Multiple of three : {multiple}')
