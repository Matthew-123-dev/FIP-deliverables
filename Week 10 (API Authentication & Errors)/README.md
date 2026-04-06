# Week 10 — API Authentication & Errors

This folder contains a small, self-contained Flask app demonstrating API error handling and a simple API-key based authentication scheme.

## At a glance
- File: `app.py` — Flask app with custom `ApiError`, centralized JSON error handlers, and example endpoints.
- Purpose: show clear error responses, input validation, and a simple `X-API-KEY` auth guard.

## Endpoints
- GET `/` — basic instructions and list of example endpoints.
- GET `/divide?numerator=..&denominator=..` — validates parameters and returns JSON with the result; returns 400 for validation errors (including division by zero).
- GET `/secure` — protected endpoint; requires `X-API-KEY` header (or `Authorization: Bearer <key>`). If `API_KEY` is not set on the server, auth is effectively disabled.

## Requirements
- Python 3.8+
- Flask (the repository-level `requirements.txt` may already include this)

## Install
From this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install Flask
```

If you prefer using the project `requirements.txt`, install that instead.

## Environment variables / .env
- `API_KEY` — (optional) the server-side API key expected by `/secure`.

You can create a `.env` in this folder with:

```properties
API_KEY='a-strong-local-secret'
```

Note: `app.py` reads `API_KEY` from `os.getenv('API_KEY')`. If `API_KEY` is not set, the `/secure` endpoint will not require a key (useful for local demos).

## Run the app

One-shot (use this shell's env vars only):

```bash
API_KEY="localtestkey" python3 app.py
```

Or export permanently in your shell before running:

```bash
export API_KEY="localtestkey"
python3 app.py
```

The app listens on port 5000 by default.

## Test the endpoints (examples)

- Division (valid):

```bash
curl "http://127.0.0.1:5000/divide?numerator=10&denominator=2"
# => {"numerator":10.0,"denominator":2.0,"result":5.0}
```

- Division (bad input):

```bash
curl -i "http://127.0.0.1:5000/divide?numerator=foo&denominator=2"
# => 400 with JSON explaining the parameter error
```

- Division (division by zero):

```bash
curl -i "http://127.0.0.1:5000/divide?numerator=1&denominator=0"
# => 400 with JSON: {"error": {"message": "Division by zero is not allowed"}}
```

- Secure endpoint without key (should return 401 when API_KEY set):

```bash
curl -i "http://127.0.0.1:5000/secure"
# => 401 Unauthorized (if API_KEY is configured server-side)
```

- Secure endpoint with key:

```bash
curl -H "X-API-KEY: localtestkey" "http://127.0.0.1:5000/secure"
# => {"secret":"you have access"}
```

## Error handling behavior
- The app raises `ApiError` for expected client errors. The `ApiError` handler returns JSON in the shape `{ "error": { "message": ..., "details": ... } }` with the configured status code.
- Common HTTP errors (400/401/404/405/500) are handled centrally and return JSON responses.
- Internal server errors avoid leaking stack traces or internal details.

## Optional improvements
- Use `python-dotenv` to auto-load `.env` files at startup (I can add this for you).
- Add unit tests to exercise error responses and auth flows.
- Add a README example showing how the JSON errors look in practice.

If you want any of those added (dotenv autoload, tests, or README examples), tell me which and I will implement them.
