from pathlib import Path
import csv
from cleaner import clean_rows


BASE_DIR = Path(__file__).parent
RAW_CSV = BASE_DIR / 'students_raw.csv'
CLEAN_CSV = BASE_DIR / 'students_cleaned.csv'
REPORT = BASE_DIR / 'cleaning_report.txt'


def read_csv(path):
    path = Path(path)
    with path.open(newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        return list(reader)


def write_csv(path, rows, fieldnames):
    path = Path(path)
    with path.open('w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def write_report(path, lines):
    path = Path(path)
    with path.open('w', encoding='utf-8') as fh:
        fh.write('Cleaning report\n')
        fh.write('================\n')
        for line in lines:
            fh.write(line + '\n')


def main():
    if not RAW_CSV.exists():
        print(f"Raw CSV not found at {RAW_CSV}")
        return

    rows = read_csv(RAW_CSV)
    cleaned, report = clean_rows(rows)

    write_csv(CLEAN_CSV, cleaned, fieldnames=['name', 'score', 'department'])
    write_report(REPORT, report + [f"\nKept {len(cleaned)} rows from {len(rows)} input rows."])

    print(f"Cleaning complete. Cleaned CSV: {CLEAN_CSV}\nReport: {REPORT}")


if __name__ == '__main__':
    main()
import csv
import re
from pathlib import Path


RAW = Path(__file__).parent / "students_raw.csv"
CLEAN = Path(__file__).parent / "students_cleaned.csv"
REPORT = Path(__file__).parent / "cleaning_report.txt"


def parse_score(raw):
    if raw is None:
        return None
    s = str(raw).strip()
    if s == "":
        return None
    # remove percentage sign
    s = s.replace('%', '')
    # common NaN markers
    if s.lower() in ("nan", "n/a", "none"):
        return None
    # remove commas
    s = s.replace(',', '')
    # try float conversion
    try:
        val = float(s)
    except ValueError:
        return None
    # scores should be 0-100
    if val < 0 or val > 100:
        return None
    # if integer-like, return int
    if val.is_integer():
        return int(val)
    return val


def clean_name(raw):
    if raw is None:
        return None
    name = str(raw).strip()
    if name == "":
        return None
    # collapse repeated spaces
    name = re.sub(r"\s+", " ", name)
    return name


def clean_department(raw):
    if raw is None:
        return None
    dept = str(raw).strip()
    if dept == "":
        return None
    dept = re.sub(r"\s+", " ", dept)
    return dept


def process():
    if not RAW.exists():
        print(f"Raw file not found: {RAW}")
        return

    cleaned = []
    report_lines = []
    with RAW.open(newline='') as fh:
        reader = csv.DictReader(fh)
        for i, row in enumerate(reader, start=2):
            orig = dict(row)
            name = clean_name(row.get('Name'))
            dept = clean_department(row.get('Department'))
            score_raw = row.get('Score')
            score = parse_score(score_raw)

            issues = []
            if name is None:
                issues.append('missing name')
            if dept is None:
                issues.append('missing department')
            if score is None:
                issues.append(f'invalid score: {score_raw}')

            if issues:
                report_lines.append(f"Line {i}: {issues} -> {orig}")

            # Decide action: keep only rows with name, department, and valid score
            if name and dept and (score is not None):
                cleaned.append({'Name': name, 'Department': dept, 'Score': score})
            else:
                # skip row (could choose to correct; for now we remove invalid)
                continue

    # write cleaned CSV
    with CLEAN.open('w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=['Name', 'Department', 'Score'])
        writer.writeheader()
        for r in cleaned:
            writer.writerow(r)

    # write report
    with REPORT.open('w') as fh:
        fh.write('Cleaning report\n')
        fh.write('================\n')
        if report_lines:
            for line in report_lines:
                fh.write(line + '\n')
        else:
            fh.write('No issues found.\n')

    print(f"Wrote cleaned CSV: {CLEAN}")
    print(f"Wrote report: {REPORT}")


if __name__ == '__main__':
    process()
