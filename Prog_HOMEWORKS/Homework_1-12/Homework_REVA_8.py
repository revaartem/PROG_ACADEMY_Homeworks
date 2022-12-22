# 1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".

days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thirsday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}

day_request = int(input('Enter number of day from 1 to 7: '))
print(days.get(day_request), "Error. Try numbers from 1 to 7.")
print('#' * 60)

# 2. Опишіть кота (домашня тварина) на основі словника.

cat = {
    'name': 'Dumpy',
    'weight, kg': 7,
    'color': 'Brown',
    'breed': 'Maine Coon',
    'age': 7,
    'parents': {
        'father': 'Jack',
        'mother': 'Rose',
    },
    'place of bitrth': {
        'country': 'Ukraine',
        'city': 'Kharkiv',
        'name of nursery': 'Lemigans cattery',
    }
}

print(f'''
Name of cat - {cat['name']}
Weight - {cat['weight, kg']} kg
Color - {cat['color']}
Breed - {cat['breed']}
Age - {cat['age']} years
Parents:
Father - {cat['parents']['father']}
Mother - {cat['parents']['mother']}
Place of birth - {cat['place of bitrth']['country']}, {cat['place of bitrth']['city']}
Name of nursery - {cat['place of bitrth']['name of nursery']}
''')
print('#' * 60)

# 3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику,
# скільки разів яка літера зустрічається в цьому рядку.
# Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.


text = input('Enter your text: ').lower()
final_list = '''
'''

for i in set(text.lower()):
    if i.isalpha() and i not in final_list:
        final_list += f'"{i}" - {text.count(i)}\n'

print(final_list)
print('#' * 60)

# 4. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери,
# які є одночасно і в першому, і в другому рядку. Наприклад, для рядків «Hello» та «World»
# на екрані мають бути літери «l» та «o».

line_1 = input('First line - ').lower()
line_2 = input('Second line - ').lower()

line_1_set = set(line_1)
line_2_set = set(line_2)

common_words = line_1_set & line_2_set
print(f'Common words in "{line_1}" and "{line_2}" is {common_words}')
print('#' * 60)


# 5. Напишіть програму, яка згенерує два списки.
# Один із числами кратними 3, інший із числами кратними 5.


def list_generator():
    even_3 = [i for i in range(300) if not i % 3]
    even_5 = [i for i in range(300) if not i % 5]
    return even_3, even_5


# 6. Створіть список із числами, які є в обох списках.


even_to_3, even_to_5 = list_generator()

result_list = list(set(even_to_3) & set(even_to_5))
result_list.sort()
print(result_list)
