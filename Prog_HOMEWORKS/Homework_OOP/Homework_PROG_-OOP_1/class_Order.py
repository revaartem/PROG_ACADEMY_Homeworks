from datetime import datetime
import random


class Order:

    def __init__(self, buyer):
        """

        :param buyer: instance class Buyer
        """
        self.name = buyer.name
        self.surname = buyer.surname
        self.total_sum = 0
        self.new_member = buyer.new_member
        self.city_of_destination = buyer.city
        self.order_data = str(datetime.now())[:-7]
        self.order_dict = {}

    def add_to_order(self, thing, count, price, new_member):
        """

        :param thing: Name of product
        :param count:Product quantity
        :param price: Product price
        :param new_member: Is buyer is new member or not
        :return: Error if product quantity < 1
        """
        if count <= 0:
            raise ValueError ('Count of product must be grater than 0.')
        else:
            if new_member:
                self.order_dict[thing] = count, price * 0.97
            else:
                self.order_dict[thing] = count, price
            if self.new_member:
                self.total_sum += price * 0.97 * count
            else:
                self.total_sum += price * count

    def making_order(self, product_list, buyer, order):
        """

        :param product_list: instance class List, where all products are located
        :param buyer: instance class Buyer
        :param order: instance class Order
        :return: the buyer's order
        """
        for num in range(0, len(product_list)):
            current_product = product_list[num]
            order.add_to_order(current_product.name, random.randint(1, 15), current_product.price, buyer.new_member)

    def __str__(self):
        """

        :return: string vision of order
        """
        check_list = '\n'.join(
            [f'{key}-------{self.order_dict[key][0]} PCS * {self.order_dict[key][1]}$' for key in self.order_dict]
            )

        return f'''
       {self.order_data}
{check_list}
Total: {self.total_sum}$
City of car destination - {self.city_of_destination}
Customer name - {self.name} {self.surname}
'''

    def __iter__(self):
        """

        :return: Iterable object
        """
        return OrderIter(self.order_dict)

    def __getitem__(self, item):
        """

        :param item: Index of element in sequence
        :return: List with lists (Name of product, quantities, price) inside
        """

        if isinstance(item, str):
            if item not in self.order_dict:
                raise ValueError (f'There is no "{item}" in this order')
            return self.order_dict[item]

        if isinstance(item, slice):
            res = []
            start = item.start or 0
            stop = item.stop or len(self.order_dict)
            step = item.step or 1

            if step == -1:
                step = 1
                for num in range(start, stop, step):
                    name_of_product = list(self.order_dict.keys())[num]
                    product_specs = (self.order_dict[name_of_product])
                    res.append([name_of_product, product_specs[0], product_specs[1]])
                return res[::-1]

            for num in range(start, stop, step):
                name_of_product = list(self.order_dict.keys())[num]
                product_specs = (self.order_dict[name_of_product])
                res.append([name_of_product, product_specs[0], product_specs[1]])
            return res

class OrderIter:

    def __init__(self, dict_order):
        """

        :param dict_order: Dictionary with all order's products
        """
        if dict_order:
            self.dict_order = dict_order
            self.first_key = list(dict_order.keys())[0]
            self.last_key = list(dict_order.keys())[-1]
            self.key_list = list(dict_order.keys())
        self.index = 0

    def __next__(self):
        """

        :return: Name of product, quantity of this product and price of product
        """
        if self.index >= len(self.key_list):
            raise StopIteration
        self.index += 1
        name_of_product = self.key_list[self.index - 1]
        return name_of_product, self.dict_order[name_of_product][0], self.dict_order[name_of_product][1]
