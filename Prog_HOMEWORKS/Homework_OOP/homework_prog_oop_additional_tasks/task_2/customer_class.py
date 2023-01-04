
class Customer:
    """

    """

    def __init__(self, name: str, phone_number: int, address: str):
        """

        :param name: Name of customer.
        :param phone_number: Phone number of customer.
        :param address: Address of customer.
        """
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        """

        :return: String vision of Customer class.
        """
        return f'''Name - {self.name}
Phone number - {self.phone_number}
Address - {self.address}'''
