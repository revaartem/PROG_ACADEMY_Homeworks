
# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка.
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.


def add_2(n, counter):
    list_final = []
    for i in range(n, counter):
        if not list_final:
            list_final.append(i)
        else:
            n += 2
            list_final.append(n)
    return list_final


def add_3(n, counter):
    list_final = []
    for i in range(n, counter + 1):
        if not list_final:
            list_final.append(i)
        else:
            n += 3
            list_final.append(n)
    return list_final


def multiple_2(n, counter):
    list_final = []
    for i in range(n, counter + 1):
        if not list_final:
            list_final.append(i)
        else:
            n *= 2
            list_final.append(n)
    return list_final


def multiple_3(n, counter):
    list_final = []
    for i in range(n, counter + 1):
        if not list_final:
            list_final.append(i)
        else:
            n *= 3
            list_final.append(n)
    return list_final


def degree_2_in_range(n, counter):
    list_final = []
    for i in range(n, counter + 1):
        if not list_final:
            list_final.append(i)
        else:
            list_final.append(i ** 2)
    return list_final


def degree_3_in_range(n, counter):
    list_final = []
    for i in range(n, counter + 1):
        if not list_final:
            list_final.append(i)
        else:
            list_final.append(i ** 3)
    return list_final


def next_number(seq: str):
    seq = [int(i) for i in seq.split(sep=',')]
    base_number = seq[0]
    number_operation = len(seq)
    if seq == add_2(base_number, number_operation):
        return add_2(base_number, number_operation + 1)[-1]

    elif seq == add_3(base_number, number_operation):
        return add_3(base_number, number_operation + 1)[-1]

    elif seq == multiple_2(base_number, number_operation):
        return multiple_2(base_number, number_operation + 1)[-1]

    elif seq == multiple_3(base_number, number_operation):
        return multiple_3(base_number, number_operation + 1)[-1]

    elif seq == degree_2_in_range(base_number, number_operation):
        return degree_2_in_range(base_number, number_operation + 1)[-1]

    elif seq == degree_3_in_range(base_number, number_operation):
        return degree_3_in_range(base_number, number_operation + 1)[-1]

    else:
        return -1


print(f"Next number of sequence 0,2,4,6,8,10,12 is {next_number('0,2,4,6,8,10,12')}")
print(f"Next number of sequence 1,4,7,10,13 is {next_number('1,4,7,10,13')}")
print(f"Next number of sequence 1,2,4,8,16,32 is {next_number('1,2,4,8,16,32')}")
print(f"Next number of sequence 1,3,9,27 is {next_number('1,3,9,27')}")
print(f"Next number of sequence 1,4,9,16,25 is {next_number('1,4,9,16,25')}")
print(f"Next number of sequence 1,8,27,64,125 is {next_number('1,8,27,64,125')}")
print(f"Next number of sequence 1, 88 is {next_number('1, 88')}")
print('#' * 60)

# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, vyj;tyyzv яких чисел він є.


def palindrome_xxx_to_xxx():
    number = 999
    switch = True
    var = {}
    keys_to_var = []
    while switch:
        for i in range(100, 1000)[::-1]:
            data = number * i
            if str(data) == str(data)[::-1]:
                var[data] = number, i
                keys_to_var.append(data)
        number -= 1
        if number < 100:
            switch -= 1
    return *(var[max(keys_to_var)]), max(keys_to_var)


res = palindrome_xxx_to_xxx()
print(f'{res[0]} * {res[1]} = {res[2]}')