import copy
import random

# 1. Написати Python-скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7.

multiples_of_seven = []
for i in range(1, 101):
    if not i % 7:
        multiples_of_seven.append(i)


print('Multiples of 7 - ', multiples_of_seven)
print('#' * 60)

# 2. Написати Python-скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).

n = int(input('Enter number: '))
number = 1
for i in range(2, n + 1):
    number *= i
print(number)
print('#' * 60)


# 3. Написати Python-скрипт, який виводить на екран таблицю множення на 5.
# Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...

first_number = 1
for i in range(1, 11):
    print(f'{first_number} x 5 = {first_number * 5}')
    first_number += 1
print('#' * 60)

# 4. Написати Python-скрипт, який виводить на екран прямокутник із '*'.
# Висота і ширина прямокутника вводяться з клавіатури.  Наприклад,
# нижче представлений прямокутник з висотою 4 та шириною 5.
# *****
# *      *
# *      *
# *****

a_side, b_side = int(input('Enter length: ')), int(input('Enter width: '))
for i in range(a_side):
    if not i or i == a_side - 1:
        print('*' * b_side)
    else:
        print('*' * 1, ' ' * (b_side - 4), '*' * 1)
print()
print('#' * 60)

# 5. Є список [0,5,2,4,7,1,3,19]. Написати Python-скрипт для підрахунку непарних цифр у ньому.

numbers = [0,5,2,4,7,1,3,19]
debt = 0

for i in numbers:
    if i % 2:
        debt += 1
print(debt)
print('#' * 60)

# 6. Створіть список випадкових чисел (розміром 4 елементи).
# Створіть другий список у два рази більше першого, де перші 4 елементи повинні дорівнювати елементам першого списку,
# а решта елементів - подвоєним значенням початкових.
# Наприклад,
# Було → [1,4,7,2]
# Стало → [1,4,7,2,2,8,14,4]

random_list = [random.randint(1, 9) for i in range(4)]
second_list = random_list + [i * 2 for i in random_list]
print(random_list)
print(second_list)
print('#' * 60)

# 7. Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць.
# Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.

wage = [random.randint(1000, 5000) for i in range(12)]
print(f'''Salary of every month: {wage}
Average salary - {sum(wage) / len(wage)}''')
print('#' * 60)

# 8. Є матриця
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9,10, 11, 12]
# [13,14, 15, 16]
# Напишіть Python-скрипт, який виведе цю матрицю на екран, обчислить та виведе суму елементів цієї матриці.

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9,10, 11, 12], [13, 14, 15, 16]]
print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}')
print(f'Score of digits in the matrix - {sum(matrix[0]) + sum(matrix[1]) + sum(matrix[2]) + sum(matrix[3])}')

print('#' * 60)
# 9. Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
mirror_list = [7,2,9,4]
mirror_list.reverse()
print(mirror_list)
print('#' * 60)


# 10. За допомогою циклів вивести на екран усі прості числа від 1 до 100.

number = 100
list_of_simple_numbers = []
for item in range(2, number + 1):
    for j in range(2, item):
        if not item % j:
            break
    else:
        list_of_simple_numbers.append(item)
print('Simple numbers - ', list_of_simple_numbers)
print('#' * 60)


# 11. Виведіть на екран «пісочний годинник», максимальна ширина якого
# зчитується з клавіатури (число непарне). У прикладі ширина дорівнює 5.
# *****
#  ***
#   *
#  ***
# *****

length_of_clock = int(input('Enter length of clock: '))
base_of_clock = copy.copy(length_of_clock)
if not length_of_clock % 2:
    print('Only odd numbers!')
else:
    while length_of_clock != 1:
        print(' ' * int((base_of_clock - length_of_clock) / 2), '*' * length_of_clock)
        length_of_clock -= 2
    while length_of_clock <= base_of_clock:
        print(' ' * int((base_of_clock - length_of_clock) / 2), '*' * length_of_clock)
        length_of_clock += 2
