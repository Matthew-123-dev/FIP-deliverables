
"""Week 11 — SQLite table creation helper.

This script demonstrates creating a small schema in SQLite using the
standard library `sqlite3` module.

Usage:
  - Initialize the database and create tables:
	  python3 app.py --init
  - Reset (drop tables and recreate):
	  python3 app.py --reset
  - Show current tables and their schema:
	  python3 app.py --show

The database file `week11.db` is created in the same directory as this file.
Reference: https://docs.python.org/3/library/sqlite3.html
"""

import sqlite3
from pathlib import Path
import argparse
import datetime


HERE = Path(__file__).parent
DB_PATH = HERE / "week11.db"


CREATE_USERS = """
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT NOT NULL UNIQUE,
	email TEXT NOT NULL UNIQUE,
	created_at TEXT NOT NULL
);
"""

CREATE_POSTS = """
CREATE TABLE IF NOT EXISTS posts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_id INTEGER NOT NULL,
	title TEXT NOT NULL,
	body TEXT NOT NULL,
	created_at TEXT NOT NULL,
	FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

CREATE_COMMENTS = """
CREATE TABLE IF NOT EXISTS comments (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	post_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	body TEXT NOT NULL,
	created_at TEXT NOT NULL,
	FOREIGN KEY(post_id) REFERENCES posts(id) ON DELETE CASCADE,
	FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""


def connect(db_path=DB_PATH):
	conn = sqlite3.connect(str(db_path))
	# Return rows as dictionaries for convenience when inspecting
	conn.row_factory = sqlite3.Row
	# Enforce foreign keys
	conn.execute("PRAGMA foreign_keys = ON;")
	return conn


def create_tables(conn):
	with conn:
		conn.execute(CREATE_USERS)
		conn.execute(CREATE_POSTS)
		conn.execute(CREATE_COMMENTS)


def drop_tables(conn):
	with conn:
		conn.execute("DROP TABLE IF EXISTS comments;")
		conn.execute("DROP TABLE IF EXISTS posts;")
		conn.execute("DROP TABLE IF EXISTS users;")


def show_schema(conn):
	cur = conn.execute("SELECT name, type, sql FROM sqlite_master WHERE type IN ('table','index') ORDER BY type, name;")
	rows = cur.fetchall()
	if not rows:
		print("No tables/indexes found.")
		return
	for r in rows:
		print(f"{r['type'].upper()}: {r['name']}")
		sql = r['sql']
		if sql:
			print(sql)
		print("-")


def seed_example_data(conn):
	now = datetime.datetime.utcnow().isoformat()
	with conn:
		cur = conn.execute("INSERT OR IGNORE INTO users (username, email, created_at) VALUES (?, ?, ?)", ("alice", "alice@example.com", now))
		alice_id = cur.lastrowid or conn.execute("SELECT id FROM users WHERE username = ?", ("alice",)).fetchone()[0]
		cur = conn.execute("INSERT OR IGNORE INTO users (username, email, created_at) VALUES (?, ?, ?)", ("bob", "bob@example.com", now))
		bob_id = cur.lastrowid or conn.execute("SELECT id FROM users WHERE username = ?", ("bob",)).fetchone()[0]

		cur = conn.execute("INSERT INTO posts (user_id, title, body, created_at) VALUES (?, ?, ?, ?)", (alice_id, "Hello", "This is Alice's first post.", now))
		post_id = cur.lastrowid

		conn.execute("INSERT INTO comments (post_id, user_id, body, created_at) VALUES (?, ?, ?, ?)", (post_id, bob_id, "Nice post, Alice!", now))


def init_db(reset=False, seed=False):
	DB_PATH.parent.mkdir(parents=True, exist_ok=True)
	conn = connect()
	if reset:
		drop_tables(conn)
	create_tables(conn)
	if seed:
		seed_example_data(conn)
	conn.close()
	print(f"Initialized database at: {DB_PATH}")


def main():
	parser = argparse.ArgumentParser(description="SQLite helper for Week 11: create and inspect tables")
	parser.add_argument("--init", action="store_true", help="Create tables if they do not exist")
	parser.add_argument("--reset", action="store_true", help="Drop all tables and recreate them")
	parser.add_argument("--show", action="store_true", help="Show current tables and schema")
	parser.add_argument("--seed", action="store_true", help="Insert example data after init")
	args = parser.parse_args()

	if args.reset:
		init_db(reset=True, seed=args.seed)
		return

	if args.init:
		init_db(reset=False, seed=args.seed)
		return

	if args.show:
		if not DB_PATH.exists():
			print("Database file not found. Run with --init to create it.")
			return
		conn = connect()
		show_schema(conn)
		conn.close()
		return

	parser.print_help()


if __name__ == "__main__":
	main()
