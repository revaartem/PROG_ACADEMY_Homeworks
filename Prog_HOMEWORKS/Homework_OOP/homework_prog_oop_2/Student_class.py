import Human_class


class Student(Human_class.Human):
    def __init__(self, name: str, surname: str, age: int, nationality: str, sex: str,
                 group: str, course: int, name_of_college: str
                 ):
        """

        :param name: Name of Student
        :param surname: Surname of Student
        :param age: Age of Student
        :param nationality: Nationality of Student
        :param sex: Gender of Student
        :param group: Group of Student
        :param course: Course of Student
        :param name_of_college: Student's name of college
        """

        super().__init__(name, surname, age, nationality, sex)
        self.group = group
        self.course = course
        self.name_of_college = name_of_college

    def __str__(self):
        """

        :return: string vision of Student
        """

        return f'''
Full name - {self.name + ' ' + self.surname}
Age - {self.age}
Nationality - {self.nationality}
Sex - {self.sex}
Group - {self.group}
Course - {self.course}
Name of college - {self.name_of_college}'''