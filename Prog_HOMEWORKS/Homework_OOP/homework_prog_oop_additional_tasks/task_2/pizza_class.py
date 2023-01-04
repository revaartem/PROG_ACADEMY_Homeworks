
class Pizza:

    def __init__(self, name: str, price: str, ingredients: str):
        """

        :param name: Name of pizza.
        :param price: Pizza's price.
        :param ingredients: Ingredients of pizza.
        """
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        """

        :return: String vision of Pizza class.
        """
        return f"""Pizza '{self.name}'
Price - {self.price}$
Ingredients - {self.ingredients}"""

