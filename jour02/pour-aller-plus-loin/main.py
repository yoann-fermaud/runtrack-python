import math  # Allows math.sqrt()


def triangle_buildable(a: float, b: float, c: float):
    if a + b > c and a + c > b and b + c > a:
        print(f'\nYour values : {a, b, c}')
        return triangle_type(a, b, c)
    else:
        print(f'We cannot make a triangle with these values.')


def triangle_type(a, b, c):
    triangle_equilateral = a == b and a == c
    triangle_isosceles = a == b or a == c or b == c
    triangle_rectangle = a * a + b * b == round(c * c) or a * a + c * c == round(b * b) or b * b + c * c == round(a * a)

    if triangle_equilateral:
        print(f'Equilateral triangle')
    elif triangle_isosceles and not triangle_rectangle:
        print(f'Isosceles triangle')
    elif triangle_rectangle and not triangle_isosceles:
        print(f'Rectangle triangle')
    elif triangle_isosceles and triangle_rectangle:
        print(f'Isosceles triangle rectangle')


triangle_buildable(7, 7, 7)              # Equilateral triangle
triangle_buildable(12, 12, 22)           # Isosceles triangle
triangle_buildable(3, 4, 5)              # Rectangle triangle
triangle_buildable(3, 3, math.sqrt(18))  # Isosceles triangle rectangle

# To use the input remove the parameters from the function triangle_type(a, b, c) -> triangle_type()
# Comment out the triangle_buildable() function lines above
# Uncomment the two lines below

# a, b, c = map(float, input('Enter three values : ').split())
# triangle_buildable(a, b, c)
