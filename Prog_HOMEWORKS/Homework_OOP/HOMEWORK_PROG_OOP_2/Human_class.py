class Human:
    def __init__(self, name: str, surname: str, age: int, nationality: str, sex: str):
        """

        :param name: Name of Human
        :param surname: Surname of Human
        :param age: Age of Human
        :param nationality: Nationality of Human
        :param sex: Gender of Human
        """

        self.name = name
        self.surname = surname
        self.age = age
        self.nationality = nationality
        self.sex = sex

    def __str__(self):
        """

        :return: string vision of Human
        """

        return f'''
Full name - {self.name + ' ' + self.surname}
Age - {self.age}
Nationality - {self.nationality}
Sex - {self.sex}
'''