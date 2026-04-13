# students.py
# Developer A — Student management
# Branch: feature/students

# The student database is a dictionary with this structure:
# {
#   "S001": {"name": "Alice", "id": "S001"},
#   "S002": {"name": "Bob",   "id": "S002"},
# }


def add_student(students: dict, name: str, student_id: str) -> dict:
    if student_id in students:
        print(f"Student {student_id} already exists.")
    else:
        students[student_id] = {
            "name": name.strip().title(),
            "id": student_id
        }
    return students


def remove_student(students: dict, student_id: str) -> dict:
    if student_id not in students:
        print(f"Student {student_id} not found.")
        return students
    else:
        del students[student_id]
        return students


def find_student(students: dict, name: str) -> list:
    filtered_students = []
    for student in students.values():
        if name.lower() in student["name"].lower():
            filtered_students.append(student)
    return filtered_students

