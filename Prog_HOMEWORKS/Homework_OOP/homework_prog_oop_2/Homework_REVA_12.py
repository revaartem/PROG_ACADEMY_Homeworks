import Student_class
import Group_class

if __name__ == "__main__":
    student_1 = Student_class.Student('Artem', 'Reva', 25, 'Ukrainian', 'Male', 'SPR-13', 3, 'HEMC')
    student_2 = Student_class.Student('Rustam', 'Said', 24, 'Ukrainian', 'Male', 'ET-12', 2, 'HEMC')
    student_3 = Student_class.Student('George', 'Cool', 37, 'Polish', 'Male', 'ET-12', 4, 'HEMC')
    student_4 = Student_class.Student('Patrik', 'Stewart', 33, 'German', 'Male', 'SPR-13', 5, 'HEMC')
    student_5 = Student_class.Student('Chester', 'Bennington', 42, 'American', 'Male', 'SPR-13', 2, 'HEMC')
    student_6 = Student_class.Student('Mike', 'Shinoda', 45, 'American', 'Male', 'ME-21', 3, 'HEMC')
    student_7 = Student_class.Student('Garet', 'Simpson', 21, 'British', 'Female', 'ME-21', 2, 'HEMC')
    student_8 = Student_class.Student('Cooler', 'Wakanda', 33, 'Wakandian', 'Female', 'ET-13', 2, 'HEMC')
    student_9 = Student_class.Student('Icey', 'Illecebra', 43, 'Egypt', 'Male', 'ME-21', 4, 'HEMC')
    student_10 = Student_class.Student('Gordon', 'Ramsey', 51, 'American', 'Male', 'ME-21', 1, 'HEMC')

    group_1 = Group_class.Group('Group 1')
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

    print('#' * 100)

    for item in group_1:
        print(item)

    for i in group_1[::-1]:
        print(i)