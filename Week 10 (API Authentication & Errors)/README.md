# Week 10 — API Authentication & Errors

This file documents the Flask app implemented in `app.py`, which demonstrates API error handling and a simple API-key based authentication scheme.

Overview
--------
The app provides a small, self-contained example of centralized JSON error handling, input validation, and a basic `X-API-KEY` authentication guard. It includes custom `ApiError` exceptions, error handlers that return consistent JSON responses, and protected endpoints that require authentication.

Why this design
----------------
- Centralizes error handling so all responses follow a consistent JSON shape.
- Validates inputs early to prevent invalid operations (e.g., division by zero).
- Uses a simple header-based auth scheme that can be toggled on/off via environment variables.
- Avoids leaking internal details or stack traces to clients.

Quick contract
--------------
- GET `/` — returns instructions and endpoint list.
- GET `/divide?numerator=..&denominator=..` — validates parameters, returns JSON result or 400 for errors.
- GET `/secure` — protected endpoint; requires `X-API-KEY` header (or `Authorization: Bearer <key>`).
- Error responses: `{ "error": { "message": ..., "details": ... } }` with appropriate HTTP status.

Setup & run
-----------
1. Install dependencies from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install Flask
```

2. Set the API key (optional; if unset, `/secure` is unprotected):

```bash
export API_KEY="localtestkey"
```

3. Run the app:

```bash
python3 app.py
```

The app listens on port 5000 by default.

Usage examples
--------------
- Division (valid):

```bash
curl "http://127.0.0.1:5000/divide?numerator=10&denominator=2"
# => {"numerator":10.0,"denominator":2.0,"result":5.0}
```

- Division (invalid input):

```bash
curl -i "http://127.0.0.1:5000/divide?numerator=foo&denominator=2"
# => 400 with JSON error
```

- Secure endpoint with key:

```bash
curl -H "X-API-KEY: localtestkey" "http://127.0.0.1:5000/secure"
# => {"secret":"you have access"}
```

Notes
-----
- `ApiError` is raised for expected client errors and returns JSON with the configured status code.
- All HTTP errors (400/401/404/405/500) are handled centrally and return consistent JSON.
- If `API_KEY` environment variable is not set, the `/secure` endpoint does not require authentication.
- See `.env` example in the folder for local configuration.

Testing suggestions
-------------------
- Add unit tests (pytest) that cover:
    - valid and invalid division parameters
    - division by zero handling
    - authentication success and failure scenarios
    - error response shape and status codes

Provided as part of Week 10 deliverable. Free to modify for your project needs.
