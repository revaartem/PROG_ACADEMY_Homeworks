# Exercise 1. Write a Python-script that displays the message “Hello world”.
print('Hello world')

print('-' * 40)

# Exercise 2. Rewrite the first script to display three any messages.
print('One')
print('Two')
print('Three')
print('-' * 40)

# Exercise 3. Write a Python-script to reads values for the length and width of a
# rectangle and returns the area of the rectangle.
length = int(input('Please, enter length of rectangle: '))
width = int(input('Please, enter width of rectangle: '))
print(f'Area of the rectangle is {length * width}')
print('-' * 40)

# Exercise 4. Write a program that requests the user to enter two numbers and
# prints the sum, product, difference and quotient of the two numbers.
def basic_op(value1, value2):
    return print(f'''Sum of numbers is {int(value1) + int(value2)}
Product of numbers is {int(value1) * int(value2)}
Diffirence of numbers is {int(value1) - int(value2)}
Quotient of numbers is {int(value1) / int(value2)}''')

basic_op(5, 2)
print('-' * 40)

# Exercise 5. Write a program that reads in the radius of a circle and prints the
# circle’s diameter, circumference and area. Use the constant value 3.14159 for π.
# Do these calculations in output statements.

def calculation_of_circle_area(radius):
    return print(f'''Diameter of circle is {radius * 2}
Circumference of circle is {3.14159 * (radius * 2)}
Area of circle is {3.14159 * (radius ** 2)}''')

calculation_of_circle_area(5)
print('-' * 40)

