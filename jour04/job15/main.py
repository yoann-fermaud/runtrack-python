L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


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


def round_number(list_name):
    for i in range(0, len_list(list_name)):
        if list_name[i] - int(list_name[i]) < 0.5:
            list_name[i] = int(list_name[i])
        else:
            list_name[i] = int(list_name[i]) + 1
    return list_name


print(f'List values in random order                            : {L}')
print(f'List values in ascending order                         : {ascending_order(L)}')
print(f'List values in ascending order and rounding to nearest : {round_number(L)}')
