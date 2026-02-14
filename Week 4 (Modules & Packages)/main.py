"""
Main Script - Student Report Generator
Uses the studenttools package to generate a complete student report.
"""

from studenttools import gradecalc, attendancetracker, performancesummary


def main():
    # Create attendance record
    attendance = attendancetracker.create_attendance_record()
    
    # ===== STUDENT 1: Matthew =====
    # Record Matthew's attendance (10 days)
    attendancetracker.mark_attendance(attendance, "Matthew", "present")
    attendancetracker.mark_attendance(attendance, "Matthew", "present")
    attendancetracker.mark_attendance(attendance, "Matthew", "present")
    attendancetracker.mark_attendance(attendance, "Matthew", "late")
    attendancetracker.mark_attendance(attendance, "Matthew", "present")
    attendancetracker.mark_attendance(attendance, "Matthew", "absent")
    attendancetracker.mark_attendance(attendance, "Matthew", "present")
    attendancetracker.mark_attendance(attendance, "Matthew", "present")
    attendancetracker.mark_attendance(attendance, "Matthew", "present")
    attendancetracker.mark_attendance(attendance, "Matthew", "present")
    
    # Matthew's grades
    matthew_grades = [95, 88, 92, 85, 90]
    
    # Generate and print Matthew's report
    matthew_summary = performancesummary.generate_summary("Matthew", matthew_grades, attendance)
    performancesummary.print_summary(matthew_summary)
    
    # ===== STUDENT 2: Kola =====
    # Record Kola's attendance (10 days)
    attendancetracker.mark_attendance(attendance, "Kola", "present")
    attendancetracker.mark_attendance(attendance, "Kola", "absent")
    attendancetracker.mark_attendance(attendance, "Kola", "absent")
    attendancetracker.mark_attendance(attendance, "Kola", "present")
    attendancetracker.mark_attendance(attendance, "Kola", "late")
    attendancetracker.mark_attendance(attendance, "Kola", "absent")
    attendancetracker.mark_attendance(attendance, "Kola", "present")
    attendancetracker.mark_attendance(attendance, "Kola", "present")
    attendancetracker.mark_attendance(attendance, "Kola", "absent")
    attendancetracker.mark_attendance(attendance, "Kola", "present")
    
    # Kola's grades
    kola_grades = [72, 68, 75, 70, 65]
    
    # Generate and print Kola's report
    kola_summary = performancesummary.generate_summary("Kola", kola_grades, attendance)
    performancesummary.print_summary(kola_summary)
    
    # ===== STUDENT 3: Virtue =====
    # Record Virtue's attendance (10 days)
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    attendancetracker.mark_attendance(attendance, "Virtue", "present")
    
    # Virtue's grades
    virtue_grades = [98, 96, 99, 95, 97]
    
    # Generate and print Virtue's report
    virtue_summary = performancesummary.generate_summary("Virtue", virtue_grades, attendance)
    performancesummary.print_summary(virtue_summary)


if __name__ == "__main__":
    main()
