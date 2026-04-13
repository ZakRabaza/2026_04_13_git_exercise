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
    """
    Remove a student from the students dictionary by their ID.

    - If the student_id does not exist, print a warning:
      "Student S999 not found." and return the dictionary unchanged.

    Args:
        students (dict): the current students database
        student_id (str): the ID of the student to remove

    Returns:
        dict: the updated students dictionary

    Example:
        >>> db = {"S001": {"name": "Alice", "id": "S001"}}
        >>> remove_student(db, "S001")
        >>> db
        {}
    """
    # TODO: implement this function
    raise NotImplementedError("remove_student is not implemented yet.")


def find_student(students: dict, name: str) -> list:
    """
    Search for students whose name contains the given string (case-insensitive).

    - Returns a list of matching student dicts.
    - Returns an empty list if no match is found.
    - The search must be case-insensitive: "alice" matches "Alice Smith".

    Args:
        students (dict): the current students database
        name (str): the search string

    Returns:
        list: a list of matching student dicts

    Example:
        >>> db = {
        ...   "S001": {"name": "Alice Smith", "id": "S001"},
        ...   "S002": {"name": "Bob Martin",  "id": "S002"},
        ... }
        >>> find_student(db, "alice")
        [{"name": "Alice Smith", "id": "S001"}]
        >>> find_student(db, "xyz")
        []
    """
    # TODO: implement this function
    raise NotImplementedError("find_student is not implemented yet.")
