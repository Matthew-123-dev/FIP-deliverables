# Week 11 — SQLite I

Small helper for creating and inspecting a local SQLite database used for Week 11 exercises.

Files
- `app.py` — CLI helper that creates a `week11.db` SQLite file and provides the following flags: `--init`, `--reset`, `--show`, `--seed`.
- `week11.db` — database file created by the script (after running `--init`).

Prerequisites
- Python 3.8+
- Optional: `sqlite3` CLI for quick inspection

Quick commands

- Initialize database (create tables):

```bash
python3 app.py --init
```

- Initialize and insert example data:

```bash
python3 app.py --init --seed
```

- Drop all tables and recreate (reset):

```bash
python3 app.py --reset
```

- Show current tables and schema:

```bash
python3 app.py --show
```

Inspect with sqlite3 CLI

```bash
sqlite3 "Week 11 (SQLite I)/week11.db"
-- then inside sqlite3:
.tables
.schema users
SELECT * FROM users;
```

Example Python query

```python
import sqlite3
conn = sqlite3.connect('Week 11 (SQLite I)/week11.db')
conn.row_factory = sqlite3.Row
cur = conn.execute('SELECT username,email FROM users')
for r in cur:
    print(r['username'], r['email'])
conn.close()
```

Seeded example data
- `users`: `alice`, `bob`
- `posts`: one post by `alice`
- `comments`: one comment by `bob` on alice's post

Design notes
- Tables: `users`, `posts`, `comments` with foreign keys and basic constraints.
- The script enforces foreign keys (`PRAGMA foreign_keys = ON`) and uses `sqlite3.Row` for convenience.

Reference
- Python sqlite3 docs: https://docs.python.org/3/library/sqlite3.html

Next steps (suggested)
- Add a tiny test script that queries the seeded data and asserts expected rows.
- Add a README example showing `SELECT` statements and output.
- Wrap DB calls in a small DAO module if expanding the project.
