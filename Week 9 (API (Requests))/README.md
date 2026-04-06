
# Course Module (Week 9)

This file documents the Weather API implemented in `weatherapi.py`.

Overview
--------
Weather API is a small Flask-based service that exposes weather data. It returns mock data by default and can fetch live data from OpenWeatherMap if you provide an API key via the `OPENWEATHER_API_KEY` environment variable.

Why this design
----------------
- Minimal dependencies: just Flask and requests.
- Graceful fallback: works without an API key (mock mode).
- Environment-based configuration: keeps secrets out of code.
- Includes a non-leaking test helper for verification.

Quick contract
--------------
- Endpoint: `GET /weather?city=CityName`
- Output: JSON with `city`, `description`, `temp_c`, and `source` (either `"mock"` or `"openweathermap"`).
- Setup: Python 3.8+, pip, optional OpenWeatherMap API key.

Usage
-----
1. Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the server:

```bash
python3 weatherapi.py
```

3. Test the endpoint:

```bash
curl "http://127.0.0.1:5000/weather?city=London"
```

4. Run the included test helper:

```bash
python3 test_weather_check.py
```

Configuration
-------------
- Set `OPENWEATHER_API_KEY` in your shell or in a `.env` file (optional).
- The app reads the env var at runtime; if present, live data is fetched.
- Use `python-dotenv` for automatic `.env` loading (see optional section below).

Security
--------
- Do NOT commit `.env` or your API key to version control.
- Add `.env` to `.gitignore`:

```text
.env
```

Optional: Auto-load `.env` with python-dotenv
----------------------------------------------
Install and configure if you prefer automatic `.env` loading:

```bash
pip install python-dotenv
```

Add at the top of `weatherapi.py`:

```python
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / '.env')
```


