#!/usr/bin/env python3
"""Quick non-leaking tester for the weather API.

This script will:
 - read `Week 9 (API (Requests))/.env` and set the OPENWEATHER_API_KEY in os.environ if present
 - import the Flask `app` from `weatherapi` and call the /weather endpoint via the test client
 - print whether a key was found (True/False), the status code, and the JSON response

It deliberately does NOT print the API key.
"""
import os
import re
from pathlib import Path

HERE = Path(__file__).parent
env_path = HERE / ".env"

key_present = False
if env_path.exists():
    txt = env_path.read_text()
    # Simple parse for OPENWEATHER_API_KEY without exposing it
    m = re.search(r"OPENWEATHER_API_KEY\s*=\s*['\"]?([^'\"\s]+)['\"]?", txt)
    if m:
        os.environ["OPENWEATHER_API_KEY"] = m.group(1)
        key_present = True

# Import the app (safe because app.run is guarded by __main__)
from weatherapi import app

client = app.test_client()
resp = client.get('/weather', query_string={'city': 'London'})

print('key_present:', key_present)
print('status_code:', resp.status_code)
try:
    print('json:', resp.get_json())
except Exception:
    print('body:', resp.data.decode())
