
# 1. Write a Python program to print the number entered by user only if the
# number entered is negative.

print('Return the number if number is negative.')
number = int(input('Enter any number: '))
print(number < 0 and number)
print(" " * 50)

# 2. Write a Python program to check if the value a is less than 20 or not.

print('''Program to check if the value a is less than 20 or not.
If value <= 20, program will print "True", if > 20 - "False"''')
number_check = int(input('Enter any number: '))

print(number_check <= 20 or False)
print(" " * 50)

# 3. Write a Python program to check if a given number is Zero or Not.

print('Program to check if a given number is Zero or Not.')
number_not_zero = int(input('Enter any number: '))
print(f'''If number = 0, program will return "True", if not equal 0 - "False"
Result of check - {number_not_zero == 0}''')
print(" " * 50)

# 4. Write a Python program to check if a given number is Even or Odd.

print('Program to check if a given number is Even or Odd.')
number_even_or_odd = int(input('Enter any number: '))
x = number_even_or_odd % 2 == 0
print(f'Number {number_even_or_odd} is even - {x}, odd - {not x}')
print(" " * 50)

#5. Write a Python program to find largest number among three numbers
# entered by user.

print('Program to find largest number among three numbers entered by user.')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
list_of_nums = [a, b, c]
print('Max value of inputed numbers is', max(list_of_nums))

