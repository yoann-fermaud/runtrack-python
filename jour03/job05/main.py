def prime_number():
    for i in range(2, 1000):

        prime_number_flag = True

        for j in range(2, i):
            if i % j == 0:
                prime_number_flag = False

        if prime_number_flag:
            print(f'{i}')


prime_number()
