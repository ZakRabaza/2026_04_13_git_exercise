#machin
# grades.py
# Developer B — Grade calculations
# Branch: feature/grades

# The grades database is a nested dictionary with this structure:
# {
#   "S001": {"Math": 85, "English": 90, "Science": 78},
#   "S002": {"Math": 60, "English": 55},
# }
import warnings

def add_grade(grades: dict, student_id: str, subject: str, score: int) -> dict:

    if score < 0 or score > 100:
        warnings.warn("Score non compris entre 0 et 100: ", score)
        return None

    if student_id not in grades:
        grades[student_id] = {subject : score}
    else:
        grades[student_id][subject] = score
    return grades


def get_average(grades: dict, student_id: str) -> float:

    average = 0.0
    for i in range (len(grades[student_id].values())):
        average += grades[student_id][i]

    average /= len(grades[student_id])
    return round(average, 2)



def get_subjects(grades: dict) -> set:
    return set(grades.values().keys())



def get_failing_students(students: dict, grades: dict, threshold: int = 50) -> list:
    result = []

    for student_id, student_data in students.items():
        name = student_data["name"]

        average = get_average(student_id, grades)


        if average is None:
            average = 0.0

        if average < threshold:
            result.append((student_id, name, average))

    # Trier par moyenne croissante
    result.sort(key=lambda x: x[2])

    return result