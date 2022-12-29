class Buyer:
    def __init__(self, name, surname, city, phone_number, new_member):
        """

        :param name: Buyer name
        :param surname: Buyer surname
        :param city: Buyer's city
        :param phone_number: Phone number of buyer
        :param new_member: Is the buyer a new member or not
        """
        self.name = name
        self.surname = surname
        self.city = city
        self.phone_number = phone_number
        self.new_member = new_member

    def __str__(self):
        """

        :return: string vision of buyer
        """
        return f'''Buyer information:
Name - {self.name}
Surname - {self.surname}
City - {self.city}
Phone number - {self.phone_number}
New member - {self.new_member} (if {self.name} {self.surname} is a new member, discount -3%)\n'''
