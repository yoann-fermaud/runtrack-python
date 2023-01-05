L_01 = [7, 11, 42, 39, 2]
L_02 = [12, 7, 22, 120, 36, 2]


def len_list(list_name):
    len_global = 0
    for _ in list_name:
        len_global += 1
    return len_global


def ascending_order(list_name):
    for i in range(0, len_list(list_name)):
        for j in range(i + 1, len_list(list_name)):
            if list_name[i] > list_name[j]:
                temp = list_name[i]
                list_name[i] = list_name[j]
                list_name[j] = temp
    return list_name


print(f'\nList values in random order  : {L_01}')
print(f'List values in ascending order : {ascending_order(L_01)}')

print(f'\nList values in random order  : {L_02}')
print(f'List values in ascending order : {ascending_order(L_02)}')
