# 🎓 Student Grade Management System (Python CLI)

This is a simple command-line application for managing students and their grades using Python’s Object-Oriented Programming features. It's designed for pre-interview assessment, showcasing your skills in:

- Python Classes & Objects
- Encapsulation (private attributes)
- Lists & Dictionaries
- CLI user interaction
- Input validation

---

## 📦 Features

- ✅ Add new students (prevents duplicate IDs)
- ✅ Add or update student grades
- ✅ List all students with average scores
- ✅ Find a student by their ID
- ✅ View the top-performing student
- ✅ Interactive CLI menu
- ✅ Clean and beginner-friendly code

---

## 🏗️ Class Design

### `Student`

| Attribute | Type     | Description                     |
|-----------|----------|---------------------------------|
| `name`    | string   | Student’s full name             |
| `student_id` | string | Unique ID for the student       |
| `__grades`  | dict    | (Private) Subject → Score map   |

| Method | Description |
|--------|-------------|
| `add_grade(subject, score)` | Add or update a grade |
| `get_average()` | Returns average of all grades |
| `display_info()` | Prints student details |
| `get_grades()` | Getter for private grades |

---

### `StudentManager`

| Attribute | Type             | Description                 |
|-----------|------------------|-----------------------------|
| `students`| List of Students | Stores all student objects  |

| Method | Description |
|--------|-------------|
| `add_student(student)` | Adds a student if ID is unique |
| `list_students()` | Displays info for all students |
| `find_student_by_id(id)` | Searches for student by ID |
| `get_top_student()` | Returns student with highest average |

---

## 🚀 How to Run

### 1. Clone the project or download the files

```bash
git clone https://github.com/Masta7200/Student-gradeMGNT
cd student-grade-system
