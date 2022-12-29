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
        """

        :param name_of_group: Name of current group
        :param max_students: Number of max size of group
        """
        self.name_of_group = name_of_group
        self.student_list = []
        self.max_student = max_students

    def add_student(self, student_card: Student_class.Student):
        """

        :param student_card: instance class Student
        :return: Error if the student wasn't found
        """
        if student_card not in self.student_list and len(self.student_list) < self.max_student:
            self.student_list.append(student_card)
            logger.info(f'Student {student_card.name} {student_card.surname} has been successfully added to student_list')
        else:
            logger.critical(f'''Student add error
student_card not in self.student_list - {student_card not in self.student_list}
len(self.student_list) < self.max_student - {len(self.student_list) < self.max_student}''')
            raise StudentAddError_class.StudentAddError

    def __getitem__(self, item):
        """

        :param item: iteration number
        :return: list with instances class Student inside
        """
        if isinstance(item, int):
            if item > len(self.student_list):
                raise IndexError
            return self.student_list[item]
        if isinstance(item, slice):
            result = []
            start = item.start or 0
            stop = item.stop or self.student_list.index(self.student_list[-1]) + 1
            step = item.step or 1

            if step == -1:
                step = 1
                for i in range(start, stop, step):
                    result.append(self.student_list[i])
                return result[::-1]

            for i in range(start, stop, step):
                result.append(self.student_list[i])

            return result

        raise TypeError

    def delete_student(self, student_card: Student_class.Student):
        """

        :param student_card: instance class Student
        :return: Error if the student wasn't found
        """
        if student_card in self.student_list:
            self.student_list.remove(student_card)
            logger.info(f'Student {student_card.name} {student_card.surname}'
                        f' has been successfully removed from student_list')
        else:
            logger.critical('Student search error')
            raise StudentSearchError_class.StudentSearchError

    def student_search(self, name: str, surname: str, age: int):
        """

        :param name: name of Student
        :param surname: surname of Student
        :param age: age of Student
        :return: True or False
        """
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
        """

        :return: string vision of Group
        """
        return f'{self.name_of_group}:\n\n' + \
               '\n'.join(map(lambda x: str(f'{x.name} {x.surname}, {x.age}'), self.student_list))
