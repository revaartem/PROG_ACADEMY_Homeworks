import Human_class


class Student(Human_class.Human):
    def __init__(self, name: str, surname: str, age: int, nationality: str, sex: str,
                 group: str, course: int, name_of_college: str
                 ):
        """

        :param name:
        :param surname:
        :param age:
        :param nationality:
        :param sex:
        :param group:
        :param course:
        :param name_of_college:
        """

        super().__init__(name, surname, age, nationality, sex)
        self.group = group
        self.course = course
        self.name_of_college = name_of_college

    def __str__(self):
        return f'''
Full name - {self.name + ' ' + self.surname}
Age - {self.age}
Nationality - {self.nationality}
Sex - {self.sex}
Group - {self.group}
Course - {self.course}
Name of college - {self.name_of_college}'''