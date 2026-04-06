## Week 13 — Mini SQLite CLI (Todo app)

This file documents a lightweight command-line todo application backed by SQLite.
It demonstrates local database creation, basic CRUD operations, and CLI patterns
for managing users and tasks.

Overview
--------
The app uses a simple two-table schema (`users` and `todos`) with foreign-key
constraints. It provides CLI commands to initialize the database, seed sample data,
and perform standard todo operations (create, read, update, delete, list).

Why this design
----------------
- Minimal dependencies: uses only Python's standard library `sqlite3`.
- Enforced data integrity: foreign keys enabled with `ON DELETE CASCADE`.
- Clear separation: users are distinct entities; todos are tied to users.
- Easy to extend: straightforward schema and command structure.

Quick contract
--------------
- **Database**: `week13.db` (created by `--init`).
- **Core commands**:
    - `add-user --username <name>` — create a user.
    - `add-task --user <name> --title <str> --notes <str>` — create a todo.
    - `list-tasks [--user <name> | --all]` — view todos.
    - `complete --id <int>` — mark task done.
    - `delete --id <int>` — remove task.
    - `stats` — summary counts.
- **Setup**: `--init` creates schema; `--seed` populates sample data.

Usage
-----
1. Initialize and seed:

```bash
python3 app.py --init
python3 app.py --seed
```

2. Common workflows:

```bash
python3 app.py add-user --username alice
python3 app.py add-task --user alice --title "Buy milk" --notes "2L"
python3 app.py list-tasks --user alice
python3 app.py complete --id 1
python3 app.py stats
```

Schema
------
- **users**: `id (PK), username, created_at`
- **todos**: `id (PK), user_id (FK), title, notes, done, created_at, due_date`

Notes
-----
- Foreign keys are enforced; deleting a user cascades to their todos.
- The `--seed` flag creates two sample users (`alice`, `bob`) and test tasks.

Extensions
----------
- Bulk-populate with `--populate N` for benchmarking.
- Due-date filtering and overdue-task detection.
- HTTP API wrapper (Flask/FastAPI).

