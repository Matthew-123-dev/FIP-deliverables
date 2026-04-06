# Week 12 — SQLite II: Query inspection & simple optimization helper

This folder contains a small Python helper (`app.py`) that connects to the
`week11.db` created in Week 11 and helps inspect query plans, create/drop
indexes, and run simple timing benchmarks to observe the effect of indexes.

## Goals
- Show `EXPLAIN QUERY PLAN` for a representative join+aggregate query
- Create/drop recommended indexes that help that query
- Run a micro-benchmark (N runs) to compare timings before/after indexing

## Prerequisites
- Python 3.8+ (uses only the standard library: `sqlite3`, `argparse`, `time`)
- A populated `week11.db` created by Week 11. By default the script looks for the database at:

```
Week 11 (SQLite I)/week11.db
```

If that file does not exist the script will exit with an informative message — run Week 11's `app.py --init --seed` to create a small test dataset.

## How to run

From the `Week 12 (SQLite II)` folder run Python with one of the flags below.

- Show EXPLAIN QUERY PLAN for the representative query:

```bash
python3 app.py --explain
```

- Create recommended indexes:

```bash
python3 app.py --create-indexes
```

- Drop the recommended indexes:

```bash
python3 app.py --drop-indexes
```

- Run a timing benchmark (default 100 runs). Use `--runs` to change the number:

```bash
python3 app.py --benchmark --runs 200
```

You can combine flags. For example, create indexes and benchmark afterwards:

```bash
python3 app.py --create-indexes --benchmark --runs 200
```

## Representative query
The helper uses this query by default (returns posts, author username, and comment counts):

```sql
SELECT p.id, p.title, u.username, COUNT(c.id) AS comment_count
FROM posts p
JOIN users u ON u.id = p.user_id
LEFT JOIN comments c ON c.post_id = p.id
GROUP BY p.id
```

This query performs:
- a scan or index lookup on `posts` (`p`)
- a lookup on `users` by primary key
- a lookup on `comments` by `post_id` (aggregate)

## Recommended indexes created by the script
- `idx_posts_user_id` on `posts(user_id)` — helps the join from posts -> users (depending on plan)
- `idx_comments_post_id` on `comments(post_id)` — helps the LEFT JOIN/aggregation
- `idx_comments_user_id` on `comments(user_id)` — optional support for other queries

Index creation is idempotent (`CREATE INDEX IF NOT EXISTS ...`) and dropping is safe (`DROP INDEX IF EXISTS ...`).

## What each function in `app.py` does (detailed)
- `connect(db_path=...)`
  - Opens a sqlite3 connection with `row_factory=sqlite3.Row` for dict-like rows.
  - Enables foreign keys with `PRAGMA foreign_keys = ON`.
  - Exits with a helpful error if the DB file is missing.

- `explain_query(conn, sql=QUERY)`
  - Runs `EXPLAIN QUERY PLAN <sql>` and prints the returned rows.
  - Use this to understand whether the query scans a table or uses an index.

- `create_indexes(conn)`
  - Executes the SQL statements in the `INDEXES` list to create helpful indexes.
  - Prints each index name as it is created.

- `drop_indexes(conn)`
  - Drops the indexes defined in `INDEXES` if they exist.

- `time_query(conn, sql=QUERY, runs=100)`
  - Runs the query `runs` times and returns a list of execution times in milliseconds.
  - Performs a warmup fetch before timing to reduce first-run overhead.

- `benchmark(conn, runs=100)`
  - Convenience wrapper that runs `time_query` and prints statistics (median, mean, min, max).

- `print_stats(times)`
  - Prints run count and simple stats using the `statistics` module.

- `main()`
  - Argument parsing and orchestration: connects to DB, optionally explains, benchmarks, creates/drops indexes, and prints results.

## Interpreting results
- `EXPLAIN QUERY PLAN` output describes whether indices are used. Look for `SEARCH ... USING INDEX` vs `SCAN`.
- On very small datasets the timing numbers will be noisy and often sub-millisecond; populate the DB with more rows to see meaningful differences.
- Indexes speed up reads at the cost of storage and slower writes. Use `EXPLAIN QUERY PLAN` to confirm relevance.

## Suggestions to measure a clear improvement
- Seed `week11.db` with many rows (thousands) before benchmarking. You can modify `Week 11 (SQLite I)/app.py` to add more seeded rows in a loop.
- Increase `--runs` (e.g., 500 or 1000) to get a stable average and reduce noise.


