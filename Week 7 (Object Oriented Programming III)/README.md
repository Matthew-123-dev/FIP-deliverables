## CourseModule (Week 7)

This file documents the `CourseModule` class implemented in `app.py`.

Overview
--------
`CourseModule` models a course module with encapsulated internal state. The
class uses private attributes for the module title, content, progress (0-100),
and completion status. Public methods provide controlled read-only access and
safe ways to update progress and content.

Why this design
----------------
- Prevents accidental external mutation of internal state.
- Ensures progress can only increase (or be explicitly marked complete).
- Provides validation for inputs to keep state consistent.

Quick contract
--------------
- Inputs: `title: str`, optional `content: str` when constructing.
- Read outputs: `title() -> str`, `content() -> str`, `progress() -> int`,
  `is_completed() -> bool`.
- Mutations: `append_content(more: str)`, `increase_progress(amount: int)`,
  `mark_complete()`.
- Error cases: `increase_progress` raises `TypeError` for non-int input and
  `ValueError` for non-positive amounts; `append_content` raises `TypeError`
  for non-string input.

Usage
-----
1. Run the demo script (it contains a small smoke test):

```bash
python3 "Week 7/app.py"
```

2. Example usage from another module:

```python
from Week_7_app import CourseModule  # adjust import path to your package layout

m = CourseModule('Intro to Testing', 'Chapter 1')
m.increase_progress(20)
print(m.progress())         # -> 20
print(m.is_completed())     # -> False
m.mark_complete()
```

Notes
-----
- There are deliberately no public setters for title/content/progress to
  discourage direct mutation. Use `append_content`, `increase_progress`, and
  `mark_complete` instead.
- Progress is capped at 100. Calling `mark_complete()` sets progress to 100
  and marks the module completed.

Testing suggestions
-------------------
- Add unit tests (pytest) that cover:
  - creating a module and reading properties
  - valid progress increases and capping at 100
  - calling `mark_complete()` sets completion and progress
  - invalid inputs raising the correct exceptions (non-int, negative, non-str)


License / provenance
--------------------
Provided as part of Week 7 deliverable. Free to modify for your project needs.
