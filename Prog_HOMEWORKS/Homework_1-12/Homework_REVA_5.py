number = input('Enter your number: ')
list_of_numbers = list(map(int, number))
half_index = int(len(list_of_numbers) / 2)
if len(list_of_numbers) % 2 != 0:
    print('Your number is not even! Please, enter even number!')
else:
    if sum(list_of_numbers[:half_index]) == sum(list_of_numbers[half_index:]):
        print('There is lucky ticket!')
    else:
        print('Not this time, try again!')
print('#' * 60)


number_to_check = input('Enter your number: ')
number_list = list(number_to_check)
reversed_list = number_list[::-1]
if number_list == reversed_list:
    print("This is palindrome!")
else:
    print("It's not a palindrome")
print('#' * 60)

x_coordinate, y_coordinate = int(input('Enter X-coordinate: ')), int(input('Enter Y-coordinate: '))
RADIUS = 4
if RADIUS ** 2 >= x_coordinate ** 2 + y_coordinate ** 2:
    print('Coordinate inside of circle.')
else:
    print('Coordinate is out of circle.')

