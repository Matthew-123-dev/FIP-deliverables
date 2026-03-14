from validators import parse_score


def clean_rows(rows):
    cleaned = []
    report_lines = []
    seen = set()
    for i, r in enumerate(rows, start=1):
        name = (r.get('name') or '').strip()
        dept = (r.get('department') or '').strip()
        raw_score = r.get('score')

        if not name:
            report_lines.append(f"Row {i}: missing name -> row removed")
            continue

        name = ' '.join([p.capitalize() for p in name.split()])

        if name in seen:
            report_lines.append(f"Row {i}: duplicate name '{name}' -> row removed")
            continue
        seen.add(name)

        score = parse_score(raw_score)
        if score is None:
            report_lines.append(f"Row {i} ({name}): invalid/missing score '{raw_score}' -> row removed")
            continue

        if score < 0 or score > 100:
            report_lines.append(f"Row {i} ({name}): score {score} out of bounds -> clipped to nearest bound")
            score = max(0.0, min(100.0, score))

        if not dept:
            dept = 'Undeclared'
            report_lines.append(f"Row {i} ({name}): missing department -> set to 'Undeclared'")

        cleaned.append({'name': name, 'score': f"{score:.1f}", 'department': dept})

    cleaned.sort(key=lambda x: x['name'])
    return cleaned, report_lines
