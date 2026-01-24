# Student Score Calculator

This small Python program interactively collects student scores, accepts optional configuration (bonus and weight), and calculates a total and a weighted average.

Files
- `app.py` — interactive program that collects scores, accepts a bonus and weight, calls `student_score_calc`, and prints results.

What the program does
- Prompts the user to add any number of numeric scores.
- Prompts for an optional bonus score (defaults to 0).
- Prompts for an optional weight factor (defaults to 0).
- Uses `student_score_calc(*scores, **config)` to compute:
  - `total`: sum(scores) + bonus
  - `average`: total / (len(scores) + weight) if the divisor is > 0, otherwise 0
- Prints the total and average or a message if no scores were entered.

Function contract (quick reference)
- Function: `student_score_calc(*scores, **config)`
- Inputs:
  - `scores`: zero or more numeric score values (floats/ints)
  - `config` (optional): dictionary with keys `bonus` (float) and `weight` (float)
- Output: dictionary with keys `total` (float) and `average` (float)
- Error modes: the interactive script will print an error message for invalid numeric input. For invalid config inputs it falls back to defaults (0.0).

Prerequisites / Required libraries
- Python 3.6 or newer is recommended. The script uses only the Python standard library — no external packages are required.

How to run
1. Open a terminal and change to the folder containing `app.py` (example path shown):

```bash
cd "Week 1 (Intermediate Functions)"
```

2. Run the program with Python 3:

```bash
python3 app.py
```

3. Follow the interactive prompts:
- Enter `y` to add a score, then type the numeric score.
- When finished entering scores, enter `n`.
- Enter a bonus (or leave blank for 0).
- Enter a weight (or leave blank for 0).

Example session

```
--- Student Score Calculator ---
Add score? (y/n): y
Enter a score: 75
Add score? (y/n): y
Enter a score: 85.5
Add score? (y/n): n
Enter bonus score (default 0): 5
Enter weight factor (default 0): 1

Results:
Total Score: 165.5
Average: 82.75
```

Notes and edge cases
- If no scores are entered the program prints: "No scores were entered." and exits.
- The average calculation divides by (number of scores + weight). If that divisor is 0 the code returns an average of 0.
- Invalid numeric inputs when entering scores produce an "Invalid number." message and allow retrying; invalid config inputs fall back to defaults.

License
- This is a small exercise script — add a license file if you plan to distribute it.

If you want, I can also add a tiny example script that calls `student_score_calc` non-interactively for automated testing.
