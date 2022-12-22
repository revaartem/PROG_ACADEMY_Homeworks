a_side = int(input('Enter value of A-side of triangle: '))
b_side = int(input('Enter value of B-side of triangle: '))
c_side = int(input('Enter value of C-side of triangle: '))

print(a_side + b_side > c_side and a_side + c_side > b_side and c_side + b_side > a_side)
print('#' * 60)

year = int(input('Enter year to check: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(366)
else:
    print(365)
print('#' * 60)


number_of_appartment = int(input('Please, enter number of appartment: '))
number_of_appartment > 144 and print('This building have appartments from 1 to 144. Please, try again.')
entrance_number = (number_of_appartment - 1) // 36 + 1
number_apartment_in_entrance = number_of_appartment - (entrance_number - 1) * 36
floor_number = (number_apartment_in_entrance - 1) // 4 + 1
serial_number_of_apartment = (number_of_appartment - 1) % 4 + 1
number_of_appartment <= 144 and print(f'Apartment number {number_of_appartment} on {floor_number} floor in {entrance_number} entrance will be {serial_number_of_apartment} from left.')

