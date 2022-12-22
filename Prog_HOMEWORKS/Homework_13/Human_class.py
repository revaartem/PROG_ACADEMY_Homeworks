class Human:
    def __init__(self, name: str, surname: str, age: int, nationality: str, sex: str):
        """

        :param name:
        :param surname:
        :param age:
        :param nationality:
        :param sex:
        """

        self.name = name
        self.surname = surname
        self.age = age
        self.nationality = nationality
        self.sex = sex

    def __str__(self):
        """

        :return:
        """

        return f'''
Full name - {self.name + ' ' + self.surname}
Age - {self.age}
Nationality - {self.nationality}
Sex - {self.sex}
'''