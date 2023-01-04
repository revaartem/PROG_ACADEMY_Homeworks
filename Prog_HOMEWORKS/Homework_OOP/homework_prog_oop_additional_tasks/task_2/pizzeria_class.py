import pizza_class


class Pizzeria:
    """
    Instance class Pizzeria have Name and menu list. Menu list can be filled from
    .txt file automatically or manually.
    """

    def __init__(self, name: str):
        """

        :param name: Name of pizzeria.
        """
        self.name = name
        self.pizza_menu = {}
        self.pizza_menu_creator()
        self.days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    def __str__(self):
        """

        :return: String vision of instance class Pizzeria.
        """
        menu_res = ''
        index = 0

        for key in self.pizza_menu:
            menu_res += f"""
{self.days_of_week[index].capitalize()}
{self.pizza_menu[key]}
"""
            index += 1

        return f'''
Pizzeria {self.name} glad to see you!
Here is our pizza-of-the-day offer:
{menu_res}'''

    def pizza_menu_creator(self):
        """
        Create menu list from file pizzas.txt.txt.\n
        For the function to work properly, name, price and ingredients in file
        must be separated by '| '.

        :return: Raises error if the source file have too much strings inside.
        """
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        index = 0

        with open('pizzas.txt') as source:
            for pizza in source:
                if index < 7:
                    data = pizza.strip().split(sep='| ')
                    new_pizza = pizza_class.Pizza(data[0], data[1], data[2])
                    self.pizza_menu[days_of_week[index]] = new_pizza
                    index += 1
                else:
                    raise ValueError ('There is only 7 days in the week, сut your pizzas.txt list down to 7')
