def number_positive_negative(number):
    if type(number) is int or type(number) is float:
        if number < 0:
            return 'Your number is negative.'
        elif number > 0:
            return 'Your number is positive.'
    else:
        return 'Type a correct value !'


print(number_positive_negative(4))
print(number_positive_negative(-5))
print(number_positive_negative("Yoann"))
