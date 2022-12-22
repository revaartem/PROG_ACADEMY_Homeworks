
from datetime import datetime


class Product:
    def __init__(self, name, year, weight, price, size, country_code):
        self.name = name
        self.year = year
        self.weight = weight
        self.price = price
        if price <= 0:
            raise ValueError ('Price must be grater than 0.')
        self.size = size
        self.country_code = country_code
        self.quantity = 1

    def __str__(self):
        return f'''Product characteristic:
Name - {self.name}
Year of manufacturing - {self.year}
Weight - {self.weight} kg
Price - {self.price} $
Size - {self.size} mm
Manufacturer's country code - {self.country_code}\n'''


class Buyer:
    def __init__(self, name, surname, city, phone_number, new_member):
        self.name = name
        self.surname = surname
        self.city = city
        self.phone_number = phone_number
        self.new_member = new_member

    def __str__(self):
        return f'''Buyer information:
Name - {self.name}
Surname - {self.surname}
City - {self.city}
Phone number - {self.phone_number}
New member - {self.new_member} (if {self.name} {self.surname} is a new member, discount -3%)\n'''


buyer_1 = Buyer('Anton', 'Golovin', 'Kiev', 88005553535, False)
buyer_2 = Buyer('Nikola', 'Tesla', 'Lviv', 38099556874, True)
buyer_3 = Buyer('Tom', 'Hanks', 'New York', 55577789, True)
print(buyer_1)
print(buyer_2)
print(buyer_3)


class Order:
    def __init__(self, buyer):
        self.name = buyer.name
        self.surname = buyer.surname
        self.total_sum = 0
        self.new_member = buyer.new_member
        self.city_of_destination = buyer.city
        self.order_data = str(datetime.now())[:-7]
        self.order_list = {}

    def product_count(self, thing, count, price, new_member):
        if count <= 0:
            raise ValueError ('Count of product must be grater than 0.')
        else:
            if new_member:
                self.order_list[thing] = count, price * 0.97
            else:
                self.order_list[thing] = count, price
            if self.new_member:
                self.total_sum += price * 0.97 * count
            else:
                self.total_sum += price * count

    def __str__(self):
        check_list = '\n'.join(
            [f'{key}-------{self.order_list[key][0]} PCS * {self.order_list[key][1]}$' for key in self.order_list]
            )

        return f'''
       {self.order_data}
{check_list}
Total: {self.total_sum}$
City of car destination - {self.city_of_destination}
Customer name - {self.name} {self.surname}
'''


product_1 = Product('Mazda MX-5', '2005', '1240', -1, '3915 x 1735 x 1225', 'JP')
product_2 = Product('Kia Ceed', '2009', '1540', 7300, '4605 x 1800 x 1475', 'SL')
product_3 = Product('Mercedes S-klass', '2015', '1945', 45000, '6499 x 1899 x 1598', 'DE')
print(product_3)
print(product_2)
print(product_1)
order_1 = Order(buyer_1)
order_1.product_count(product_1.name, 0, product_1.price, buyer_1.new_member)
order_1.product_count(product_2.name, 13, product_2.price, buyer_1.new_member)
order_1.product_count(product_3.name, 6, product_3.price, buyer_1.new_member)

order_2 = Order(buyer_2)
order_2.product_count(product_1.name, 8, product_1.price, buyer_2.new_member)
order_2.product_count(product_2.name, 14, product_2.price, buyer_2.new_member)
order_2.product_count(product_3.name, 12, product_3.price, buyer_2.new_member)

order_3 = Order(buyer_3)
order_3.product_count(product_1.name, 1, product_1.price, buyer_3.new_member)
order_3.product_count(product_2.name, 19, product_2.price, buyer_3.new_member)
order_3.product_count(product_3.name, 16, product_3.price, buyer_3.new_member)

print(order_1)
print(order_2)
print(order_3)