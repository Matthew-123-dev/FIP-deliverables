
"""Week 12 — SQLite II: Query inspection and simple optimization helper.

This script connects to the `week11.db` created in Week 11 and helps you:
- show EXPLAIN QUERY PLAN for a representative query
- create/drop helpful indexes
- benchmark the query before/after indexes to observe improvements

Usage examples:
  python3 app.py --explain
  python3 app.py --create-indexes
  python3 app.py --benchmark --runs 200
  python3 app.py --drop-indexes

The representative query returns posts with author username and number of comments:

  SELECT p.id, p.title, u.username, COUNT(c.id) AS comment_count
  FROM posts p
  JOIN users u ON u.id = p.user_id
  LEFT JOIN comments c ON c.post_id = p.id
  GROUP BY p.id

See https://docs.python.org/3/library/sqlite3.html for details on the sqlite3 module.
"""

import sqlite3
from pathlib import Path
import argparse
import time
import statistics
import sys


HERE = Path(__file__).parent
DB_PATH = HERE.parent / "Week 11 (SQLite I)" / "week11.db"

QUERY = """
SELECT p.id, p.title, u.username, COUNT(c.id) AS comment_count
FROM posts p
JOIN users u ON u.id = p.user_id
LEFT JOIN comments c ON c.post_id = p.id
GROUP BY p.id
"""

INDEXES = [
	("idx_posts_user_id", "CREATE INDEX IF NOT EXISTS idx_posts_user_id ON posts(user_id);"),
	("idx_comments_post_id", "CREATE INDEX IF NOT EXISTS idx_comments_post_id ON comments(post_id);"),
	("idx_comments_user_id", "CREATE INDEX IF NOT EXISTS idx_comments_user_id ON comments(user_id);"),
]


def connect(db_path=DB_PATH):
	if not db_path.exists():
		raise SystemExit(f"Database not found at {db_path}. Run Week 11 init first.")
	conn = sqlite3.connect(str(db_path))
	conn.row_factory = sqlite3.Row
	conn.execute("PRAGMA foreign_keys = ON;")
	return conn


def explain_query(conn, sql=QUERY):
	cur = conn.execute(f"EXPLAIN QUERY PLAN {sql}")
	rows = cur.fetchall()
	print("EXPLAIN QUERY PLAN:")
	for r in rows:
		# sqlite returns columns: selectid, order, from, detail (names vary)
		print(tuple(r))


def create_indexes(conn):
	with conn:
		for name, stmt in INDEXES:
			print(f"Creating index: {name}")
			conn.execute(stmt)


def drop_indexes(conn):
	with conn:
		for name, _ in INDEXES:
			print(f"Dropping index if exists: {name}")
			conn.execute(f"DROP INDEX IF EXISTS {name};")


def time_query(conn, sql=QUERY, runs=100):
	# Warmup
	conn.execute(sql).fetchall()
	times = []
	for _ in range(runs):
		t0 = time.perf_counter()
		conn.execute(sql).fetchall()
		t1 = time.perf_counter()
		times.append((t1 - t0) * 1000.0)  # ms
	return times


def benchmark(conn, runs=100):
	print(f"Benchmarking query ({runs} runs)...")
	times = time_query(conn, runs=runs)
	print_stats(times)


def print_stats(times):
	print(f"runs: {len(times)}")
	print(f"median: {statistics.median(times):.3f} ms")
	print(f"mean: {statistics.mean(times):.3f} ms")
	print(f"min: {min(times):.3f} ms")
	print(f"max: {max(times):.3f} ms")


def main():
	parser = argparse.ArgumentParser(description="SQLite query inspection and simple optimization helper")
	parser.add_argument("--explain", action="store_true", help="Show EXPLAIN QUERY PLAN for the representative query")
	parser.add_argument("--create-indexes", action="store_true", help="Create recommended indexes")
	parser.add_argument("--drop-indexes", action="store_true", help="Drop the recommended indexes")
	parser.add_argument("--benchmark", action="store_true", help="Run timing benchmark for the representative query")
	parser.add_argument("--runs", type=int, default=100, help="Number of runs for benchmark")
	args = parser.parse_args()

	try:
		conn = connect()
	except SystemExit as e:
		print(e)
		sys.exit(1)

	if args.explain:
		explain_query(conn)

	if args.benchmark:
		print("-- before indexes --")
		benchmark(conn, runs=args.runs)

	if args.create_indexes:
		create_indexes(conn)
		print("Indexes created.")

	if args.benchmark and args.create_indexes:
		print("-- after indexes --")
		benchmark(conn, runs=args.runs)

	if args.drop_indexes:
		drop_indexes(conn)
		print("Indexes dropped.")

	conn.close()


if __name__ == "__main__":
	main()
