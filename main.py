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
    
    def show_menu():
     print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
     print("1. Add new student")
     print("2. Add grade to student")
     print("3. List all students")
     print("4. Find student by ID")
     print("5. Get top student")
     print("6. Exit")
 
    def main():
        manager = StudentManager()

        while True:
            StudentManager.show_menu()
            choice = input("Choose an option (1-6): ")

            if choice == "1":
                name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                student = Student(name, student_id)
                manager.add_student(student)

            elif choice == "2":
                student_id = input("Enter student ID to add grade: ")
                student = manager.find_student_by_id(student_id)
                if student:
                    subject = input("Enter subject name: ")
                    try:
                        score = float(input("Enter score (0-100): "))
                        if 0 <= score <= 100:
                            existing_grades = student.get_grades()
                            if subject in existing_grades:
                                print(f" Updating existing grade for '{subject}' (Old: {existing_grades[subject]})")
                            else:
                                print(f" Adding new grade for '{subject}'")
                            student.add_grade(subject, score)
                            print(" Grade saved successfully.")
                        else:
                            print(" Score must be between 0 and 100.")
                    except ValueError:
                        print(" Invalid score format.")
                else:
                    print(" Student not found.")

            elif choice == "3":
                manager.list_students()

            elif choice == "4":
                student_id = input("Enter student ID to find: ")
                student = manager.find_student_by_id(student_id)
                if student:
                    student.display_info()
                else:
                    print(" Student not found.")

            elif choice == "5":
                top_student = manager.get_top_student()
                if top_student:
                    print(" Top Student:")
                    top_student.display_info()
                else:
                    print(" No students in the system.")

            elif choice == "6":
                print("Thanks for using our system . Goodbye!")
                break

            else:
                print(" Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    StudentManager.main()
