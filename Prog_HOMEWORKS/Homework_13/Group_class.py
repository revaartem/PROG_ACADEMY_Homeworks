import logging
import Student_class
import StudentAddError_class
import StudentSearchError_class

logger = logging.getLogger('log_of_students')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
filehandler = logging.FileHandler('logger.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)


class Group:
    def __init__(self, name_of_group: str, max_students=10):
        self.name_of_group = name_of_group
        self.student_list = []
        self.max_student = max_students

    def add_student(self, student_card: Student_class.Student):
        if student_card not in self.student_list and len(self.student_list) < self.max_student:
            self.student_list.append(student_card)
            logger.info(f'Student {student_card.name} {student_card.surname} has been successfully added to student_list')
        else:
            logger.critical(f'''Student add error
student_card not in self.student_list - {student_card not in self.student_list}
len(self.student_list) < self.max_student - {len(self.student_list) < self.max_student}''')
            raise StudentAddError_class.StudentAddError

    def delete_student(self, student_card: Student_class.Student):
        if student_card in self.student_list:
            self.student_list.remove(student_card)
            logger.info(f'Student {student_card.name} {student_card.surname}'
                        f' has been successfully removed from student_list')
        else:
            logger.critical('Student search error')
            raise StudentSearchError_class.StudentSearchError

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
        return f'{self.name_of_group}:\n\n' + \
               '\n'.join(map(lambda x: str(f'{x.name} {x.surname}, {x.age}'), self.student_list))

