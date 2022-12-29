class Product:
    def __init__(self, name, year, weight, price, size, country_code):
        """

        :param name: Product name
        :param year: Year of manufacturing
        :param weight: Weight of product
        :param price: Price of product
        :param size: Size of product
        :param country_code: Country of manufacturing
        """
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
        """

        :return: string vision of product
        """
        return f'''Product characteristic:
Name - {self.name}
Year of manufacturing - {self.year}
Weight - {self.weight} kg
Price - {self.price} $
Size - {self.size} mm
Manufacturer's country code - {self.country_code}\n'''
