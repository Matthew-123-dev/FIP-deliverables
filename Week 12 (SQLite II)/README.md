# Week 12 — SQLite II: Query inspection & simple optimization helper

This file documents the query optimization helper (`app.py`) that connects to the `week11.db` database and demonstrates `EXPLAIN QUERY PLAN`, index creation, and timing benchmarks.

Overview
--------
The helper connects to a populated SQLite database and provides tools to inspect query execution plans, create/drop indexes, and measure query performance before and after optimization. It focuses on a representative join+aggregate query to show the practical impact of indexing.

Why this design
----------------
- Demonstrates how `EXPLAIN QUERY PLAN` reveals whether queries use indexes or full table scans.
- Isolates index creation logic in a reusable helper to avoid manual SQL.
- Uses micro-benchmarking to quantify performance gains from indexing on real data.
- Validates database existence upfront to prevent silent failures.

Quick contract
--------------
- Inputs: command-line flags (`--explain`, `--create-indexes`, `--drop-indexes`, `--benchmark`, `--runs`).
- Read outputs: query plans, execution times (milliseconds), statistics (median, mean, min, max).
- Database path: looks for `Week 11 (SQLite I)/week11.db` by default.
- Error cases: exits with informative message if database file is missing.

Usage
-----
From the `Week 12 (SQLite II)` folder, run:

```bash
python3 app.py --explain                    # Show query plan
python3 app.py --create-indexes             # Create indexes
python3 app.py --drop-indexes               # Drop indexes
python3 app.py --benchmark --runs 200       # Time the query (200 runs)
python3 app.py --create-indexes --benchmark --runs 200  # Create then measure
```

Notes
-----
- On small datasets (< 1000 rows), timing will be noisy and sub-millisecond.
- Seed the database with thousands of rows for meaningful benchmark results.
- Indexes are created idempotently and dropped safely with `IF [NOT] EXISTS`.
- Run `Week 11 (SQLite I)/app.py --init --seed` first if `week11.db` does not exist.

Testing suggestions
-------------------
- Verify `EXPLAIN QUERY PLAN` shows `SEARCH ... USING INDEX` after index creation.
- Run `--benchmark` before and after `--create-indexes` to measure improvement.
- Increase row count and `--runs` to reduce timing variance and detect real gains.
- Test that missing `week11.db` triggers a helpful error message.

License / provenance
--------------------
Provided as part of Week 12 deliverable. Free to modify for your project needs.
