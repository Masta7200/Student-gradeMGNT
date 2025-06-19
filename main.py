class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = {}  # private dictionary
    def add_grade(self, subject, score):
        self.__grades[subject] = score
