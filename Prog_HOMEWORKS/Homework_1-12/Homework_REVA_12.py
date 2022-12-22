import logging

logger = logging.getLogger('log_of_students')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
filehandler = logging.FileHandler('logger.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')



class Human:
    def __init__(self, name: str, surname: str, age: int, nationality: str, sex: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.nationality = nationality
        self.sex = sex

    def __str__(self):
        return f'''
Full name - {self.name + ' ' + self.surname}
Age - {self.age}
Nationality - {self.nationality}
Sex - {self.sex}
'''


class Student(Human):
    def __init__(self, name: str, surname: str, age: int, nationality: str, sex: str,
                 group: str, course: int, name_of_college: str
                 ):
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


student_1 = Student('Artem', 'Reva', 25, 'Ukrainian', 'Male', 'SPR-13', 3, 'HEMC')
student_2 = Student('Rustam', 'Said', 24, 'Ukrainian', 'Male', 'ET-12', 2, 'HEMC')
student_3 = Student('George', 'Cool', 37, 'Polish', 'Male', 'ET-12', 4, 'HEMC')
student_4 = Student('Patrik', 'Stewart', 33, 'German', 'Male', 'SPR-13', 5, 'HEMC')
student_5 = Student('Chester', 'Bennington', 42, 'American', 'Male', 'SPR-13', 2, 'HEMC')
student_6 = Student('Mike', 'Shinoda', 45, 'American', 'Male', 'ME-21', 3, 'HEMC')
student_7 = Student('Garet', 'Simpson', 21, 'British', 'Female', 'ME-21', 2, 'HEMC')
student_8 = Student('Cooler', 'Wakanda', 33, 'Wakandian', 'Female', 'ET-13', 2, 'HEMC')
student_9 = Student('Icey', 'Illecebra', 43, 'Egypt', 'Male', 'ME-21', 4, 'HEMC')
student_10 = Student('Gordon', 'Ramsey', 51, 'American', 'Male', 'ME-21', 1, 'HEMC')


class StudentAddError(Exception):
    def __init__(self):
        self.message = None

    def __str__(self):
        return 'This student is already in this group!'


class StudentSearchError(Exception):
    def __init__(self):
        self.message = None

    def __str__(self):
        return 'This student is not in this group!'


class Group:
    def __init__(self, name_of_group: str, max_students=10):
        self.name_of_group = name_of_group
        self.student_list = []
        self.max_student = max_students

    def add_student(self, student_card: Student):
        """

        :param student_card:
        :return:
        """
        if student_card not in self.student_list:
            self.student_list.append(student_card)
            logger.info('Student has been successfully added to student_list')
        else:
            logger.critical('Student add error')
            raise StudentAddError

    def delete_student(self, student_card: Student):
        if student_card in self.student_list:
            self.student_list.remove(student_card)
            logger.info('Student has been successfully removed from student_list')
        else:
            logger.critical('Student search error')
            raise StudentSearchError

    def student_search(self, name: str, surname: str, age: int):
        if not self.student_list:
            logger.critical('Empty student list error')
            raise ValueError ('List is empty.')
        for student_card in self.student_list:
            if student_card.name == name and student_card.surname == surname and student_card.age == age:
                logger.info(f'Searching for {student_card.name + " " + student_card.surname}')
                return True
            else:
                return False

    def __str__(self):
        return ''.join([f'{student_card.name + " " + student_card.surname}\n' for student_card in self.student_list])


group_1 = Group('Grupa')
group_1.add_student(student_1)
group_1.add_student(student_2)
group_1.add_student(student_3)
group_1.add_student(student_4)
group_1.add_student(student_5)
group_1.add_student(student_6)
group_1.add_student(student_7)
group_1.add_student(student_8)
group_1.add_student(student_9)
group_1.add_student(student_10)
print(group_1)

print(group_1.student_search('Artem', 'Reva', 25))
print(group_1.student_search('Artem', 'Reva', 25))
