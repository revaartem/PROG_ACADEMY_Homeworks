import customer_class
import pizzeria_class
import random


class Order:
    """
    Instance class Order contains all information about customer,
    pizzeria and makes it possible to create order list with all
    positions, that customer want. Also, adding some funny joke
    at the end of every order check.
    """

    def __init__(self, customer: customer_class.Customer, pizzeria: pizzeria_class.Pizzeria):
        """

        :param customer: instance class Customer
        :param pizzeria: instance class Pizzeria
        """
        self.name = customer.name
        self.menu = pizzeria.pizza_menu
        self.pizzeria_name = pizzeria.name
        self.total_sum = 0
        self.customer_phone_number = customer.phone_number
        self.customer_address = customer.address
        self.delivery_time = 'As far as possible.'
        self.order = {}
        self.jokes = []

        with open('jokes.txt', encoding='utf-8') as source:
            for joke in source:
                self.jokes.append(joke.strip())

    def add_to_order(self, day_of_the_week: str, quantity: int,
                     extra_cheese: int = 0, extra_sauce: int = 0, extra_bacon: int = 0, delivery_time: str = ''):
        """

        :param day_of_the_week: Day of the week, for simple pizza selection
        :param quantity: Quantity of current position
        :param extra_cheese: Add extra cheese or not. Default - 0. Every portion cost 3$
        :param extra_sauce: Add extra sauce or not. Default - 0. Every portion cost 2$
        :param extra_bacon: Add extra bacon or not. Default - 0. Every portion cost 4$
        :param delivery_time: Time of delivery. Default - 'As far as possible.'.
        :return: Raises error if incorrect pizza name or incorrect quantity.
        """
        pizza = self.menu.get(day_of_the_week.lower())
        if pizza is None:
            raise ValueError (f'There is no {day_of_the_week} pizza in our menu.')
        price = pizza.price
        if quantity <= 0:
            raise ValueError('Quantity of the product must be grater than 0.')
        self.order[pizza.name] = (quantity, price, extra_cheese, extra_sauce, extra_bacon)
        if delivery_time:
            self.delivery_time = delivery_time
        self.total_sum += (int(price) + (extra_bacon * 4) + (extra_cheese * 3) + (extra_sauce * 2)) * int(quantity)

    def __str__(self):
        """

        :return: String vision of Order class.
        """
        res = ''
        for key in self.order:
            res += f'''{key}{'-' * (30 - len(key)) } {self.order[key][0]} PCS * {self.order[key][1]}$\n'''

            if self.order[key][2]:  # If extra cheese added
                res += f"{6 * ' '}Extra cheese x {self.order[key][2]}" \
                       f"{'-' * (7 + len(str(self.order[key][2])))} {self.order[key][2] * self.order[key][0] * 3}$\n"

            if self.order[key][3]:  # If extra sauce added
                res += f"{6 * ' '}Extra sauce x {self.order[key][3]}" \
                       f"{'-' * (8 + len(str(self.order[key][3])))} {self.order[key][3] * self.order[key][0] * 2}$\n"

            if self.order[key][4]:  # If extra bacon added
                res += f"{6 * ' '}Extra bacon x {self.order[key][4]}" \
                       f"{'-' * (8 + len(str(self.order[key][4])))} {self.order[key][4] * self.order[key][0] * 4}$\n"

        return f"""
     Pizzeria "{self.pizzeria_name}"
        
Customer - {self.name}
Delivery address - {self.customer_address}
Phone number - {self.customer_phone_number}
Delivery time - {self.delivery_time}

{res}
Total: {self.total_sum}$

Joke of the day: 
{random.choice(self.jokes)}
"""
