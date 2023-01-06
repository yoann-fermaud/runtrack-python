import math


def student_grade(list_grade):
    void_list_grade = []

    for i in range(len(list_grade)):
        if list_grade[i] > 40:
            if list_grade[i] % 5 < 3:
                void_list_grade.append(list_grade[i])
            else:
                multiple = math.ceil(list_grade[i] / 5) * 5
                void_list_grade.append(multiple)
        else:
            void_list_grade.append(list_grade[i])

    return void_list_grade


L = [22, 56, 64, 62, 72, 88, 43]
print(student_grade(L))
