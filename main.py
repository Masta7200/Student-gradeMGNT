class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = {}  # private dictionary
        
    def add_grade(self, subject, score):
        self.__grades[subject] = score

    def get_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades.values()) / len(self.__grades)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Grades:")
        for subject, score in self.__grades.items():
            print(f"  {subject}: {score}")
        print(f"Average: {self.get_average():.2f}")

    def get_grades(self):
        return self.__grades.copy()
    
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if self.find_student_by_id(student.student_id):
            print(f" Student with ID {student.student_id} already exists please try different.")
        else:
            self.students.append(student)
            print(f" Student {student.name} added successfully.")

    def list_students(self):
        if not self.students:
            print("No students added yet.")
        for student in self.students:
            student.display_info()
            print("------")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average())