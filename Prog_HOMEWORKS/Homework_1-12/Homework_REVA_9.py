

# 1. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.


def concatination(number_1, number_2, data):
    return f'{number_1 + number_2}{data}'


print(concatination(4, 5, 'lesson'))
print('#' * 60)


# 2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.

def star_art(length, width):
    for i in range(length):
        if not i or i == length - 1:
            print('*' * width)
        else:
            print('*' * 1, ' ' * (width - 4), '*' * 1)


star_art(3, 7)
print('#' * 60)


# 3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».


def searching_element(list_of_search, element):
    if element in list_of_search:
        return list_of_search.index(element)
    else:
        return -1


print(searching_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 3))
print(searching_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10))
print('#' * 60)

# 4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.


def word_count(data):
    return len(data.split())


print(word_count('Hello my lovely darling'))
print('#' * 60)


# 5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів,
# в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents


def money_sound(money):
    money_dict = {
        '$': 'dollars ',
        'C': 'cents ',
        0: '',
        1: 'one ',
        2: 'two ',
        3: 'three ',
        4: 'four ',
        5: 'five ',
        6: 'six ',
        7: 'seven ',
        8: 'eight ',
        9: 'nine ',
        10: 'ten ',
        11: 'eleven ',
        12: 'twelve ',
        13: 'thirteen ',
        14: 'fourteen ',
        15: 'fifteen ',
        16: 'sixteen ',
        17: 'seventeen ',
        18: 'eighteen ',
        19: 'nineteen ',
        20: 'twenty ',
        30: 'thirty ',
        40: 'forty ',
        50: 'fifty ',
        60: 'sixty ',
        70: 'seventy ',
        80: 'eighty ',
        90: 'ninety ',
        100: 'hundred ',
        1000: 'thousand ',
        1000000: 'million ',
    }
    print(str(money))
    list_of_money = str(money).split(sep='.')
    if len(list_of_money[1]) == 1:
        list_of_money[1] += '0'
    print(str(money))

    money_translated = ''

    ceil = int(list_of_money[0])
    last_100 = ceil % 10
    decent_100 = ceil % 100 - last_100
    if decent_100 == 10:
        decent_100 += last_100
        last_100 = False
    hundred_100 = ceil % 1000 // 100
    last_100_000 = ceil // 1000 % 10
    decent_100_000 = ceil // 1000 % 100 - last_100_000
    if decent_100_000 == 10:
        decent_100_000 += last_100_000
        last_100_000 = False
    hundred_100_000 = ceil // 1000 % 1000 // 100
    last_100_000_000 = ceil // 1000000 % 10
    decent_100_000_000 = ceil // 1000000 % 100 - last_100_000_000
    if decent_100_000_000 == 10:
        decent_100_000_000 += last_100_000_000
        last_100_000_000 = False
    hundred_100_000_000 = ceil // 1000000 % 1000 // 100

    millions = [hundred_100_000_000, decent_100_000_000, last_100_000_000]
    thousands = [hundred_100_000, decent_100_000, last_100_000]
    hundreds = [hundred_100, decent_100, last_100]

    for index, value in enumerate(millions):
        if not sum(millions):
            break
        elif value and not index:
            money_translated += money_dict[value] + money_dict[100]
        elif index == 2:
            money_translated += money_dict[value] + money_dict[1000000]
        else:
            money_translated += money_dict[value]

    for index, value in enumerate(thousands):
        if not sum(thousands):
            break
        elif value and not index:
            money_translated += money_dict[value] + money_dict[100]
        elif index == 2:
            money_translated += money_dict[value] + money_dict[1000]
        else:
            money_translated += money_dict[value]

    for index, value in enumerate(hundreds):
        if not sum(hundreds):
            break
        elif value and not index:
            money_translated += money_dict[value] + money_dict[100]
        elif index == 2:
            money_translated += money_dict[value] + money_dict['$']
        else:
            money_translated += money_dict[value]

    if len(list_of_money) == 2:
        last_1 = int(list_of_money[1]) % 10
        decent_1 = int(list_of_money[1]) % 100 - last_1
        if decent_1 == 10:
            decent_1 += last_1
            last_1 = False
        cents = [decent_1, last_1]

        for index, value in enumerate(cents):
            if not sum(cents):
                break
            elif index == 1:
                money_translated += money_dict[value] + money_dict['C']
            else:
                money_translated += money_dict[value]

    return money_translated


print(money_sound(0.9))
print('#' * 60)

# 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22
# Докладніше: https://en.wikipedia.org/wiki/Roman_numerals


def romanian_to_arabic(number):
    arabic_number = 0
    rome_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for index, value in enumerate(number):
        if value == 'C' and index + 1 < len(number):
            if number[index + 1] == 'D' or number[index + 1] == 'M':
                arabic_number -= rome_dict[value]
            else:
                arabic_number += rome_dict[value]
        elif value == 'X' and index + 1 < len(number):
            if number[index + 1] == 'L' or number[index + 1] == 'C':
                arabic_number -= rome_dict[value]
            else:
                arabic_number += rome_dict[value]
        elif value == 'I' and index + 1 < len(number):
            if number[index + 1] == 'V' or number[index + 1] == 'X':
                arabic_number -= rome_dict[value]
            else:
                arabic_number += rome_dict[value]
        else:
            arabic_number += rome_dict[value]

    return arabic_number


romanian_numbers = ['XXXIX', 'CCXLVI', 'DCCLXXXIX',
                    'MMCDXXI', 'CLX', 'CCVII', 'MIX',
                    'MLXVI', 'MDCCLXXVI', 'MCMXVIII',
                    'MCMLIV', 'MMXIV', 'MMMCMXCIX', 'MMXXII']


for i in romanian_numbers:
    print(f'The number {i} in arabic will be {romanian_to_arabic(i)}')
