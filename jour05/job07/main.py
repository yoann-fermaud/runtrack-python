def dictionary(word):
    void_list     = []
    len_word      = len(word)
    len_void_list = len(void_list)

    for i in range(len_word):
        void_list.append(word[i])

    flag = True
    iteration = 0

    while flag:
        if void_list[len_void_list - 1] != void_list[len_void_list - 2]:
            (void_list[len_void_list - 2], void_list[len_void_list - 1]) = (void_list[len_void_list - 1],
                                                                            void_list[len_void_list - 2])
            flag = False
        else:
            while void_list[len_void_list - 1] == void_list[len_void_list - 1 - iteration]:
                iteration += 1

            (void_list[len_void_list - iteration], void_list[len_void_list - 1 - iteration]) = (void_list[len_void_list - 1 - iteration],
                                                                                                void_list[len_void_list - iteration])
            flag = False

    return ''.join(void_list)


word = input(f"Choose your word : ")
print(dictionary(word))
