L = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]


def list_L():
    L[3] = L[2] + L[4]
    print(f'After list_L : {L}')
    return L[3]


print(f'L[1] value : {L[1]}')
print(f'Before list_L : {L}')
list_L()
print(f'Last element of the list L[] : {L[-1]}')
