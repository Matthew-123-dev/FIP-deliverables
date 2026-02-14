"""
Student Attendance Tracker Module
A simple module for tracking student attendance.
"""


def create_attendance_record():
    """
    Create a new empty attendance record.
    
    Returns:
        An empty dictionary to store attendance data
    """
    return {}


def mark_attendance(record, student_name, status):
    """
    Mark a student's attendance for a day.
    
    Args:
        record: The attendance record dictionary
        student_name: The student's name
        status: Attendance status ('present', 'absent', 'late')
    """
    if student_name not in record:
        record[student_name] = []
    record[student_name].append(status.lower())


def get_attendance_rate(record, student_name):
    """
    Calculate a student's attendance rate.
    
    Args:
        record: The attendance record dictionary
        student_name: The student's name
        
    Returns:
        Attendance rate as a percentage (0-100), or 0 if no records
    """
    if student_name not in record or not record[student_name]:
        return 0
    
    attendance_list = record[student_name]
    present_count = attendance_list.count("present") + attendance_list.count("late")
    return (present_count / len(attendance_list)) * 100


def get_total_absences(record, student_name):
    """
    Get the total number of absences for a student.
    
    Args:
        record: The attendance record dictionary
        student_name: The student's name
        
    Returns:
        Number of absences
    """
    if student_name not in record:
        return 0
    return record[student_name].count("absent")


