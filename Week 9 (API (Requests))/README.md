
# Weather API (minimal)

Small Flask-based API that exposes:

- GET / -> short instructions
- GET /weather?city=CityName -> returns mock data by default. If you set
  `OPENWEATHER_API_KEY` (OpenWeatherMap API key) the app will fetch live data.

## Prerequisites

- Python 3.8+ and pip
- A valid OpenWeatherMap API key if you want live data (optional)

## Install

From the `Week 9 (API (Requests))` folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## .env file (optional)

You said you already added a `.env` in this folder. The project will read
the `OPENWEATHER_API_KEY` environment variable at runtime. A simple `.env`
format that the included test script understands is:

```properties
OPENWEATHER_API_KEY='YOUR_KEY_HERE'
```

Notes:
- The app itself uses `os.getenv('OPENWEATHER_API_KEY')`. If the env var is set,
  live data is used; if not, the app returns mock data.
- The provided `test_weather_check.py` reads the `.env` file (without
  printing the secret) and sets the env var for the test run.

## Run the server

Basic (uses whatever env vars are set in your shell):

```bash
python3 weatherapi.py
```

One-shot (set a key for this command only):

```bash
OPENWEATHER_API_KEY="YOUR_KEY" python3 weatherapi.py
```

Persistent (bash):

```bash
echo 'export OPENWEATHER_API_KEY="YOUR_KEY"' >> ~/.bashrc
source ~/.bashrc
```

## Quick test (non-leaking)

There is a small helper script included: `test_weather_check.py`.

- What it does: loads `.env` (if present) and sets `OPENWEATHER_API_KEY` in the
  process, imports the Flask `app` and calls `/weather?city=London` via the
  Flask test client, and prints three lines: whether a key was present,
  the HTTP status code, and the JSON response. It does NOT print the key.

Run it like this:

```bash
python3 test_weather_check.py
```

Expected output example:

```
key_present: True
status_code: 200
json: {'city': 'London', 'description': 'overcast clouds', 'source': 'openweathermap', 'temp_c': 15.98}
```

- If `key_present` is `True` and `source` is `openweathermap` in the JSON,
  your key worked and live data was fetched.
- If `key_present` is `False` the app will return mock data (source: `mock`).

## Try the endpoint directly (curl)

Start the server (see "Run the server" above), then:

```bash
curl "http://127.0.0.1:5000/weather?city=London"
```

If live mode is active the JSON will include `"source": "openweathermap"`.

## Optional: load `.env` automatically with python-dotenv

If you'd prefer the app to auto-load the `.env` file, install `python-dotenv`
and add a couple of lines at the top of `weatherapi.py` (example shown here,
but you only need this if you want the behavior):

```bash
pip install python-dotenv
```

Add near the top of `weatherapi.py`:

```python
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / '.env')
```

I can make this change for you if you want.

## Security / housekeeping

- Do NOT commit your `.env` or API key to version control. Add `.env` to
  your `.gitignore` if you haven't already:

```text
.env
```

- The repository does not (and should not) contain your API key.

## Next steps I can help with

- Add `python-dotenv` support automatically and add `.env` to `.gitignore`.
- Add a tiny unit test that mocks the OpenWeather response.
- Add a Dockerfile for easy runs.

Tell me which of the above you'd like and I'll implement it.
