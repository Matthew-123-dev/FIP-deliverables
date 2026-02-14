# Week 4: Modules & Packages

This week's deliverable focuses on understanding and implementing **Python modules and packages**. The project demonstrates how to organize code into reusable, modular components through two practical examples: a Student Tools package and a Games package.

## 📁 Project Structure

```
Week 4 (Modules & Packages)/
├── main.py                 # Student report generator script
├── game_launcher.py        # Game selection menu script
├── studenttools/           # Student management package
│   ├── __init__.py
│   ├── gradecalc.py
│   ├── attendancetracker.py
│   └── performancesummary.py
└── games/                  # Mini-games package
    ├── __init__.py
    ├── guess_number.py
    ├── dice_roll.py
    └── rps.py
```

## 🎓 Student Tools Package (`studenttools/`)

A package for managing student grades, attendance, and generating performance summaries.

### Modules

#### `gradecalc.py` - Grade Calculator
- `calculate_average(grades)` - Calculate the average of a list of grades
- `get_letter_grade(score)` - Convert numeric score (0-100) to letter grade (A-F)
- `calculate_gpa(letter_grades)` - Calculate GPA on a 4.0 scale from letter grades

#### `attendancetracker.py` - Attendance Tracker
- `create_attendance_record()` - Create a new empty attendance record
- `mark_attendance(record, student_name, status)` - Mark attendance as 'present', 'absent', or 'late'
- `get_attendance_rate(record, student_name)` - Calculate attendance rate as a percentage
- `get_total_absences(record, student_name)` - Get total number of absences

#### `performancesummary.py` - Performance Summary Generator
- `get_performance_level(average_grade, attendance_rate)` - Determine performance level (Excellent, Good, Satisfactory, Needs Improvement, At Risk)
- `generate_summary(student_name, grades, attendance_record)` - Generate a complete performance summary dictionary
- `print_summary(summary)` - Print a formatted performance report

### Usage Example

Run the student report generator:
```bash
python main.py
```

This generates performance reports for three sample students (Matthew, Kola, and Virtue), displaying their grades, attendance rates, and overall performance levels.

---

## 🎮 Games Package (`games/`)

A package containing fun mini-games demonstrating module organization.

### Modules

#### `guess_number.py` - Guess the Number
- Try to guess a random number between 1 and 100
- Limited to 7 attempts
- Provides "too high" or "too low" hints

#### `dice_roll.py` - Dice Roll
- Roll virtual dice with customizable options
- Configure number of dice and sides per die
- Displays individual results and total

#### `rps.py` - Rock-Paper-Scissors
- Play the classic game against the computer
- Tracks score across multiple rounds
- Displays final results and winner

### Usage Example

Run the game launcher:
```bash
python game_launcher.py
```

This displays an interactive menu to select and play any of the three games.

---

## 🎯 Learning Objectives

This project demonstrates:

1. **Creating Packages** - Organizing related modules into packages with `__init__.py` files
2. **Module Imports** - Using relative imports (`from . import module`) within packages
3. **Package Imports** - Importing modules from packages (`from package import module`)
4. **Code Organization** - Separating concerns into distinct, reusable modules
5. **Docstrings** - Documenting modules and functions for clarity

## 🚀 How to Run

```bash
# Run the student report generator
python main.py

# Run the game launcher
python game_launcher.py
```

## 📝 Key Concepts

### Package Structure
- A package is a directory containing an `__init__.py` file
- The `__init__.py` file can import submodules to make them accessible

### Import Styles Used
```python
# Importing specific modules from a package
from studenttools import gradecalc, attendancetracker, performancesummary

# Using relative imports within a package
from . import gradecalc
```

### Benefits of Modular Design
- **Reusability** - Modules can be imported and used in multiple scripts
- **Maintainability** - Changes to one module don't affect others
- **Readability** - Code is organized logically by functionality
- **Testability** - Individual modules can be tested in isolation
