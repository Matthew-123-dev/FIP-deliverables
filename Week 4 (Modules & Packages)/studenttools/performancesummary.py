"""
Student Performance Summary Module
A simple module for generating student performance summaries.
"""

from . import gradecalc
from . import attendancetracker


def get_performance_level(average_grade, attendance_rate):
    """
    Determine overall performance level based on grades and attendance.
    
    Args:
        average_grade: The student's average grade (0-100)
        attendance_rate: The student's attendance rate (0-100)
        
    Returns:
        A performance level string
    """
    combined_score = (average_grade * 0.7) + (attendance_rate * 0.3)
    
    if combined_score >= 90:
        return "Excellent"
    elif combined_score >= 80:
        return "Good"
    elif combined_score >= 70:
        return "Satisfactory"
    elif combined_score >= 60:
        return "Needs Improvement"
    else:
        return "At Risk"


def generate_summary(student_name, grades, attendance_record):
    """
    Generate a complete performance summary for a student.
    
    Args:
        student_name: The student's name
        grades: A list of numeric grades
        attendance_record: The attendance record dictionary
        
    Returns:
        A dictionary containing all performance metrics
    """
    average = gradecalc.calculate_average(grades)
    letter_grade = gradecalc.get_letter_grade(average)
    attendance_rate = attendancetracker.get_attendance_rate(attendance_record, student_name)
    absences = attendancetracker.get_total_absences(attendance_record, student_name)
    performance_level = get_performance_level(average, attendance_rate)
    
    return {
        "student_name": student_name,
        "grades": grades,
        "average": average,
        "letter_grade": letter_grade,
        "attendance_rate": attendance_rate,
        "total_absences": absences,
        "performance_level": performance_level
    }


def print_summary(summary):
    """
    Print a formatted performance summary.
    
    Args:
        summary: A summary dictionary from generate_summary()
    """
    print(f"\n{'='*40}")
    print(f"  STUDENT PERFORMANCE REPORT")
    print(f"{'='*40}")
    print(f"  Student: {summary['student_name']}")
    print(f"{'='*40}")
    print(f"  GRADES")
    print(f"  ------")
    print(f"  Scores: {summary['grades']}")
    print(f"  Average: {summary['average']:.2f}")
    print(f"  Letter Grade: {summary['letter_grade']}")
    print(f"{'='*40}")
    print(f"  ATTENDANCE")
    print(f"  ----------")
    print(f"  Attendance Rate: {summary['attendance_rate']:.1f}%")
    print(f"  Total Absences: {summary['total_absences']}")
    print(f"{'='*40}")
    print(f"  OVERALL PERFORMANCE: {summary['performance_level']}")
    print(f"{'='*40}\n")


