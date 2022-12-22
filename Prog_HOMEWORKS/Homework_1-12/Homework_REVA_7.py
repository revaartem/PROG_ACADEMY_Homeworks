import string
import math


# 1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.

text = input('Enter your text: ')
counter = text.lower().count('b')
print(f'In your text "B" letter has been used for {counter} times')
print('#' * 60)


# 2. Користувач вводить з клавіатури ім'я людини.
# Написати програму для перевірки введеного ім'я на валідність (мається на увазі, що,
# наприклад, в імені людини не може бути цифр, воно повинно починатися з великої літери,
# за якою повинні йти маленькі).


name_inp = input('Enter your name: ')
title = name_inp.istitle()
validation = True
for index, char in enumerate(name_inp):
    if not index and not title:
        print('Your name must started from Upper-case letter!')
        validation = False
        continue
    elif char in string.punctuation or char in string.digits:
        print('Name can only contain letters!')
        validation = False
        break

if validation:
    print('Your name is valid.')
print('#' * 60)


#3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.

data_str = input('Enter your string: ')
score = 0
for i in data_str:
    score += ord(i)
print(f'Your score is {score}')
print('#' * 60)


#  Виведіть на екран 10 рядків із значенням числа Pi.
#  У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.

after_dot = 3
for _ in range(10):
    print(f'{math.pi:.{after_dot}}')
    after_dot += 1
print('#' * 60)


# 5. Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.

users_text = input('Enter your text: ')
list_of_user_text = users_text.split()
len_of_words = [len(i) for i in list_of_user_text]
print(list_of_user_text[len_of_words.index(max(len_of_words))])
print('#' * 60)


# Додаткові задачі до домашнього завдання:
# 1. Вовочка, сидячи на уроці, писав поспіль однакові слова
# (слово може складатися з однієї літери). Коли Марія Іванівна
# забрала у нього зошит, там був один рядок тексту. Напишіть програму,
# яка визначить найкоротше слово з написаних Вовочкою.
#
# Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"


space_out_text = 'levellevel'
decoded_word = ''
index_v = 1

for i in space_out_text:
    if space_out_text[index_v - 1] == space_out_text[index_v] and space_out_text[0:index_v] ==\
            space_out_text[index_v:index_v + len(space_out_text[0:index_v])]:  # Testing for doubled,
        # tripled or more starting of the word
        if i.count(space_out_text) == len(space_out_text):  # Test to know, is the word palindrome or not
            decoded_word += space_out_text[0:1]
            print('The word is', decoded_word)
            break
        else:
            decoded_word += space_out_text[0:index_v]
            print('The word is', decoded_word)
            break
    elif space_out_text[0:index_v] != space_out_text[index_v:index_v + len(space_out_text[0:index_v])]:  # Matching pare of
        # words
        index_v += 1
    else:
        decoded_word += space_out_text[0:index_v]  # Final result if all conditions are met
        print('The word is', decoded_word)
        break


print('#' * 60)


# 2. Напишіть програму для очищення тексту від HTML-тегів.
# Більше про html-теги https://html5book.ru/html-tags/
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто.
# перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації. Наприклад <div id="rcnt"
# style="clear:both;position:relative;zoom:1">


html_text = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" 
  "http://www.w3.org/TR/html4/loose.dtd">nskc
<html>scm
 <head>skmc
  <title>Тег BODY, атрибут text</title>skmc
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">slmc
 </head>smc
 <body text="maroon">skmc
  <p>Пример текста</p>smc
 </body>ksmc
</html>"""

text_without_tags = ''
delete_marker = 0

for i in html_text:
    if i == '<':
        delete_marker += 1
        continue
    elif i == '>':
        delete_marker -= 1
        continue
    elif delete_marker:
        continue
    else:
        text_without_tags += i

print(text_without_tags)
