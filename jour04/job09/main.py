L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

maximum_L = L[0]
minimum_L = L[0]

for i in range(len(L)):
    if L[i] > maximum_L:
        maximum_L = L[i]
    elif L[i] < minimum_L:
        minimum_L = L[i]

print(f'Maximum number : {maximum_L}\nMinimum number : {minimum_L}')
