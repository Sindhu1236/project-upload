class Student:
    def __init__(self, sid, name):
        self.__sid = sid
        self.__name = name

    def get_name(self):
        return self.__name

    def display(self):
        print("ID:", self.__sid)
        print("Name:", self.__name)


class Subject:
    def __init__(self, s1, s2, s3):
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3

    def average(self):
        return (self.__s1 + self.__s2 + self.__s3) / 3


class GradeCalculator:
    def calculate_grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"


class ReportCard:
    def show(self, student, subject):
        student.display()

        avg = subject.average()

        grade = GradeCalculator().calculate_grade(avg)

        print("Average:", avg)
        print("Grade:", grade)


# Driver Code
student = Student(101, "Rahul")
subject = Subject(85, 90, 80)

report = ReportCard()
report.show(student, subject)