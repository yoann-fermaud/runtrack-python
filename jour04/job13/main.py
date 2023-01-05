L_01 = [2, 7, 11, 42, 39, 2]
L_02 = ["cupcake", "candy", "lollipop", "cake", "lollipop", "cheesecake", "candy", "cupcake"]


def del_duplicate(list_name):
    void_list = []
    for i in list_name:
        if i not in void_list:
            void_list += [i]
    return void_list


print(f'\nBefore the function del_duplicate : {L_01}')
print(f'After the function del_duplicate    : {del_duplicate(L_01)}')

print(f'\nBefore the function del_duplicate : {L_02}')
print(f'After the function del_duplicate    : {del_duplicate(L_02)}')
