"""
Student Grade Calculator Module
A simple module for calculating student grades.
"""


def calculate_average(grades):
    """
    Calculate the average of a list of grades.
    
    Args:
        grades: A list of numeric grades
        
    Returns:
        The average grade as a float, or 0 if the list is empty
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)


def get_letter_grade(score):
    """
    Convert a numeric score to a letter grade.
    
    Args:
        score: A numeric score (0-100)
        
    Returns:
        A letter grade (A, B, C, D, or F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_gpa(letter_grades):
    """
    Calculate GPA from a list of letter grades.
    
    Args:
        letter_grades: A list of letter grades (A, B, C, D, F)
        
    Returns:
        The GPA as a float (4.0 scale)
    """
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    
    if not letter_grades:
        return 0.0
    
    total_points = sum(grade_points.get(grade.upper(), 0) for grade in letter_grades)
    return total_points / len(letter_grades)

