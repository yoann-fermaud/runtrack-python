import math


# --| 1 |-- #
def len_wc_v(number_step, height_step):
    frequency = 5
    day_per_week = 7
    len_total = 0

    for j in range(frequency):
        len_step = height_step * math.sqrt(2)
        len_step *= number_step
        len_step *= 2
        len_total += len_step
    len_total *= day_per_week / 100

    return print(f'For {number_step} steps of {height_step} cm, '
                 f'the lighthouse keeper travels {round(len_total, 2)} m per week.')


len_wc_v(22, 20)


# --| 2 |-- #
def len_wc(number_step, height_step):
    frequency = 5
    day_per_week = 7
    len_total = 0

    for i in range(day_per_week):
        for j in range(frequency):
            len_step = height_step * math.sqrt(2)
            len_step *= number_step
            len_step *= 2
            len_total += len_step / 100

    return print(f'For {number_step} steps of {height_step} cm, '
                 f'the lighthouse keeper travels {round(len_total, 2)} m per week.')


len_wc(222, 20)
