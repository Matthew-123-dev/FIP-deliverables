## Week 11 — SQLite I

This file documents the SQLite database helper implemented in `app.py`.

Overview
--------
A small helper for creating and inspecting a local SQLite database used for
Week 11 exercises. The script manages table creation, seeding example data,
and provides inspection tools for the `week11.db` database file.

Why this design
----------------
- Centralizes database initialization and reset logic in a single CLI tool.
- Enforces foreign key constraints and consistent schema across setups.
- Provides quick inspection without requiring manual SQL queries.
- Seeds realistic example data for testing queries.

Quick contract
--------------
- Files: `app.py` (CLI helper), `week11.db` (created database).
- CLI flags: `--init` (create tables), `--reset` (drop and recreate),
    `--show` (display schema), `--seed` (insert example data).
- Tables: `users`, `posts`, `comments` with foreign keys and constraints.
- Seeded data: users `alice` and `bob`; one post by alice; one comment by bob.

Usage
-----
1. Initialize the database:

```bash
python3 app.py --init
```

2. Initialize and seed example data:

```bash
python3 app.py --init --seed
```

3. Reset (drop all tables and recreate):

```bash
python3 app.py --reset
```

4. Inspect schema:

```bash
python3 app.py --show
```

5. Query with sqlite3 CLI:

```bash
sqlite3 "Week 11 (SQLite I)/week11.db"
.tables
.schema users
SELECT * FROM users;
```

6. Query from Python:

```python
import sqlite3
conn = sqlite3.connect('Week 11 (SQLite I)/week11.db')
conn.row_factory = sqlite3.Row
cur = conn.execute('SELECT username,email FROM users')
for r in cur:
        print(r['username'], r['email'])
conn.close()
```

Notes
-----
- Requires Python 3.8+.
- Enforces `PRAGMA foreign_keys = ON` for referential integrity.
- Uses `sqlite3.Row` for convenient attribute-style column access.
- Optional: install `sqlite3` CLI for quick schema inspection.

Testing suggestions
-------------------
- Add a test script that queries seeded data and asserts expected rows.
- Add README examples showing `SELECT` statements and output.
- Wrap DB calls in a small DAO module if expanding the project.

Reference
---------
- Python sqlite3 docs: https://docs.python.org/3/library/sqlite3.html

