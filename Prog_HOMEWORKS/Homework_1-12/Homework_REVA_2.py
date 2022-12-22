import math

# 1. Construct an integer from the string "123"
data_int = int('123')
print(type(data_int))
print('-' * 40)

# 2. Construct a float from the integer 123
data_float = float('123')
print(type(data_float))
print('-' * 40)

# 3. Construct an integer from the float 12.345
data_float_to_int = int(12.345)
print(type(data_float_to_int))
print('-' * 40)

# 4. Write a Python-script that detects the last 4 digits of a credit card
def last_4_nums(number):
    return int(str(number)[-4:])

print(last_4_nums(1234567890123456))
print('-' * 40)

# 5. Write a Python-script that calculates the sum of the digits of a three-digit
# number

def sum_of_digits(num):
    return sum([int(i) for i in str(num)])

print(sum_of_digits(456))
print('-' * 40)

# 6. Write a program that calculates and displays the area of a triangle if its sides
# are known
def area_of_right_triangle(a_side, b_side):
    return (0.5 * a_side * b_side)

def area_of_triangle_geron_formula(a_side, b_side, c_side):
    semi_perimetr = 0.5 * (a_side + b_side + c_side)
    return math.sqrt(semi_perimetr * (semi_perimetr - a_side) * (semi_perimetr - b_side) * (semi_perimetr - c_side))

print('Area of right triangle:', area_of_right_triangle(12, 14))
print('Area of triangle by Geron method:', area_of_triangle_geron_formula(5, 5, 5))
print('-' * 40)

# 7. *Write a Python-script that calculates the sum of the digits of a number
def sum_of_digits(num):
    return sum([int(i) for i in str(num)])

print(sum_of_digits(45651613163841313413413134513413156))
print('-' * 40)

# 8. *Determine the number of digits in a number
print(len(str(6841384138413841385)))
print('-' * 40)

# 9. *Print the digits in reverse order
data = 13513138516531
reversed = ''.join(reversed(str(data)))
print(reversed)
print('-' * 40)