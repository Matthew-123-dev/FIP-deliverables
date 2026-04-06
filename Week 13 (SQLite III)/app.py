"""Week 13 — Mini SQLite-powered CLI app (todo list)

Features:
- Create a local SQLite DB `week13.db` and tables for `users` and `todos`.
- CLI commands to add/list/complete/delete tasks and manage users.
- Simple seeding mode for quick testing.

Usage examples:
  python3 app.py --init
  python3 app.py --seed
  python3 app.py add-user --username alice
  python3 app.py add-task --user alice --title "Buy milk" --notes "2L"
  python3 app.py list-tasks --user alice
  python3 app.py complete --id 1
  python3 app.py stats
"""

import sqlite3
from pathlib import Path
import argparse
import datetime
import sys

HERE = Path(__file__).parent
DB_PATH = HERE / "week13.db"


SCHEMA_USERS = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
"""

SCHEMA_TODOS = """
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    notes TEXT,
    done INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    due_date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""


def connect(path=DB_PATH):
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(seed=False):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = connect()
    with conn:
        conn.execute(SCHEMA_USERS)
        conn.execute(SCHEMA_TODOS)
    conn.close()
    print(f"Initialized database at: {DB_PATH}")
    if seed:
        seed_data()


def seed_data():
    conn = connect()
    now = datetime.datetime.utcnow().isoformat()
    with conn:
        conn.execute("INSERT OR IGNORE INTO users (username, created_at) VALUES (?, ?)", ("alice", now))
        conn.execute("INSERT OR IGNORE INTO users (username, created_at) VALUES (?, ?)", ("bob", now))
        alice = conn.execute("SELECT id FROM users WHERE username = ?", ("alice",)).fetchone()[0]
        conn.execute("INSERT INTO todos (user_id, title, notes, created_at) VALUES (?, ?, ?, ?)", (alice, "Buy milk", "2L semi-skimmed", now))
        conn.execute("INSERT INTO todos (user_id, title, notes, created_at) VALUES (?, ?, ?, ?)", (alice, "Read emails", None, now))
    conn.close()
    print("Seeded sample users and todos")


def add_user(username):
    conn = connect()
    now = datetime.datetime.utcnow().isoformat()
    try:
        with conn:
            conn.execute("INSERT INTO users (username, created_at) VALUES (?, ?)", (username, now))
        print(f"User created: {username}")
    except sqlite3.IntegrityError:
        print(f"User already exists: {username}")
    finally:
        conn.close()


def add_task(username, title, notes=None, due_date=None):
    conn = connect()
    user = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
    if not user:
        print(f"No such user: {username}")
        conn.close()
        return
    user_id = user[0]
    now = datetime.datetime.utcnow().isoformat()
    with conn:
        cur = conn.execute("INSERT INTO todos (user_id, title, notes, created_at, due_date) VALUES (?, ?, ?, ?, ?)", (user_id, title, notes, now, due_date))
        todo_id = cur.lastrowid
    conn.close()
    print(f"Added task {todo_id} for {username}: {title}")


def list_tasks(username=None, show_all=False):
    conn = connect()
    q = "SELECT t.id, u.username, t.title, t.notes, t.done, t.created_at, t.due_date FROM todos t JOIN users u ON u.id = t.user_id"
    params = ()
    if username and not show_all:
        q += " WHERE u.username = ?"
        params = (username,)
    q += " ORDER BY t.done, t.created_at DESC"
    cur = conn.execute(q, params)
    rows = cur.fetchall()
    if not rows:
        print("No tasks found.")
        conn.close()
        return
    for r in rows:
        status = "✓" if r[4] else " "
        due = f" (due {r['due_date']})" if r['due_date'] else ""
        print(f"[{status}] id={r['id']} user={r['username']} title={r['title']}{due}")
        if r['notes']:
            print(f"    notes: {r['notes']}")
    conn.close()


def complete_task(todo_id):
    conn = connect()
    with conn:
        cur = conn.execute("UPDATE todos SET done = 1 WHERE id = ? AND done = 0", (todo_id,))
        if cur.rowcount == 0:
            print(f"No pending task with id={todo_id}")
        else:
            print(f"Completed task id={todo_id}")
    conn.close()


def delete_task(todo_id):
    conn = connect()
    with conn:
        cur = conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        if cur.rowcount == 0:
            print(f"No task with id={todo_id}")
        else:
            print(f"Deleted task id={todo_id}")
    conn.close()


def stats():
    conn = connect()
    cur = conn.execute("SELECT COUNT(*) as total, SUM(done) as done FROM todos")
    r = cur.fetchone()
    total = r['total'] or 0
    done = r['done'] or 0
    print(f"Tasks: total={total}, done={done}, pending={total-done}")
    conn.close()


def parse_args():
    p = argparse.ArgumentParser(description="Mini SQLite todo CLI (Week 13)")
    p.add_argument("--init", action="store_true", help="Create database and tables")
    p.add_argument("--seed", action="store_true", help="Seed example data (requires --init or existing DB)")
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser("add-user")
    a.add_argument("--username", required=True)

    b = sub.add_parser("add-task")
    b.add_argument("--user", required=True, help="username")
    b.add_argument("--title", required=True)
    b.add_argument("--notes", default=None)
    b.add_argument("--due", default=None, help="due date string")

    c = sub.add_parser("list-tasks")
    c.add_argument("--user", default=None)
    c.add_argument("--all", action="store_true", help="Show tasks for all users")

    d = sub.add_parser("complete")
    d.add_argument("--id", type=int, required=True)

    e = sub.add_parser("delete")
    e.add_argument("--id", type=int, required=True)

    f = sub.add_parser("stats")

    return p.parse_args()


def main():
    args = parse_args()
    if args.init:
        init_db()
        if args.seed:
            seed_data()
        return

    if args.seed:
        seed_data()
        return

    if args.cmd == "add-user":
        add_user(args.username)
        return

    if args.cmd == "add-task":
        add_task(args.user, args.title, notes=args.notes, due_date=args.due)
        return

    if args.cmd == "list-tasks":
        list_tasks(username=args.user, show_all=args.all)
        return

    if args.cmd == "complete":
        complete_task(args.id)
        return

    if args.cmd == "delete":
        delete_task(args.id)
        return

    if args.cmd == "stats":
        stats()
        return

    print("No action specified. Use --help for usage.")


if __name__ == "__main__":
    main()
