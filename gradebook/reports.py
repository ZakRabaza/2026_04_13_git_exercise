# reports.py
# Developer C — Reporting & summaries
# Branch: feature/reports


students = {
"S001": {"name": "Alice", "id": "S001"},
"S002": {"name": "Bob", "id": "S002"},
}
grades = {"S001": {"Math": 90}, "S002": {"Math": 70}}



"""
Return the top n students with the highest average scores.

- Returns a list of (student_id, name, average) tuples.
- Sorted by average in descending order (highest first).
- If n is greater than the number of students, return all of them.
- Students with no grades have an average of 0.0.

Args:
    students_param (dict): the students database
    grades_param (dict): the grades database
    n (int): number of top students to return (default 3)

Returns:
    list[tuple]: list of (student_id, name, average) sorted descending

Example:
    #>>> students = {
    #...   "S001": {"name": "Alice", "id": "S001"},
    #...   "S002": {"name": "Bob",   "id": "S002"},
    #... }
    #>>> grades = {"S001": {"Math": 90}, "S002": {"Math": 70}}
    #>>> get_top_students(students, grades, n=1)
    [("S001", "Alice", 90.0)]


    How sorted works
    iterable 	Required. The sequence to sort, list, dictionary, tuple etc.
    key 	    Optional. A Function to execute to decide the order. Default is None
    reverse 	Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

    here :  grades_param.items() is a dictionary (iterable)
            key is a lamba expression saying that the item[1]
"""


def get_top_students(students_param: dict, grades_param: dict, n: int = 3) -> list:
    result = []

    for student_id, student_info in students_param.items():     #get a tuple from items
        name = student_info['name']
        student_grades = grades_param.get(student_id,{})    #if student has no grades -> {}
        if student_grades:  #Evaluates if a dictionary contains items (True) or if is empty (False). If true calculate average
            scores = student_grades.values()
            average = sum(scores)/len(scores)
        else:       #Average = 0.0
            average = 0.0
        result.append((student_id, name, average))      #Append tuple to result
    result.sort(key=lambda item: item[2], reverse=True) #Sort the list by average desc
    return result[:n]




'''
students = {                                                #Dictionary of dictionaries
"S001": {"name": "Alice", "id": "S001"},
"S002": {"name": "Bob", "id": "S002"},
"S003": {"name": "Charlie", "id": "S003"},
"S004": {"name": "David", "id": "S004"},
}
grades = {"S001": {"Math": 90}, "S002": {"Math": 70}, "S003": {"Math": 20}}       #Dictionary of dictionaries
#grades = {"S001": {"Math": 90,"Chemistry":80}, "S002": {"Math": 70,"Chemistry":90}, "S003": {"Math": 20}}       #Dictionary of dictionaries
'''



def summarize_class(students_param: dict, grades_param: dict) -> tuple:

    """
    Return a summary of the whole class as a single tuple.

    The tuple must contain exactly 4 values in this order:
        (total_students, class_average, highest_average, lowest_average)

    - total_students (int): number of students in the database
    - class_average (float): average of all students' averages, rounded to 2 decimals
    - highest_average (float): the best individual average in the class
    - lowest_average (float): the worst individual average in the class

    - If there are no students, return (0, 0.0, 0.0, 0.0).

    Args:
        students_param (dict): the students database
        grades_param (dict): the grades database

    Returns:
        tuple: (total_students, class_average, highest_average, lowest_average)

    Example:
        students = {
        ...   "S001": {"name": "Alice", "id": "S001"},
        ...   "S002": {"name": "Bob",   "id": "S002"},
        ... }
        grades = {"S001": {"Math": 80}, "S002": {"Math": 60}}
        summarize_class(students, grades)
        (2, 70.0, 80.0, 60.0)
    """

def export_report(students_param: dict, grades_param: dict) -> str:
    """
    Generate and return a formatted text report as a single string.

    The report must follow this exact format:
    ─────────────────────────────────
    GRADEBOOK REPORT
    Total students: 3
    Class average:  75.33

    STUDENT DETAILS
    S001 | Alice Smith     | Avg:  85.00 | Subjects: English, Math, Science
    S002 | Bob Martin      | Avg:  62.50 | Subjects: Math, Science
    S003 | Carol White     | Avg:   0.00 | Subjects: none
    ─────────────────────────────────

    Rules:
    - Student names are left-aligned in a field of 16 characters.
    - Averages are right-aligned with 2 decimal places.
    - Subjects are listed in alphabetical order, comma-separated.
    - If a student has no grades, show "none" for subjects.
    - Use summarize_class() to get total_students and class_average.
    - Students are listed in alphabetical order by name.

    Args:
        students_param (dict): the students database
        grades_param (dict): the grades database

    Returns:
        str: the complete formatted report
    """
