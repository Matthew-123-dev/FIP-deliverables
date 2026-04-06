"""Minimal Weather API using Flask.

Endpoints:
 - GET /             -> brief instructions
 - GET /weather?city=Name -> returns weather for city (mock by default). If
   you set environment variable OPENWEATHER_API_KEY the app will fetch live
   data from OpenWeatherMap instead.

Contract:
 - input: query param `city` (string)
 - output: JSON with `city`, `temp_c`, `description`, and `source`
 - error modes: 400 for missing params, 502 for upstream failures, 500 for server errors
"""
from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)


@app.route("/")
def index():
	return jsonify({
		"app": "weatherapi",
		"message": "Use GET /weather?city=CityName (optional: set OPENWEATHER_API_KEY for live data)"
	})


@app.route("/weather")
def get_weather():
	city = request.args.get("city", "").strip()
	if not city:
		return jsonify({"error": "missing 'city' query parameter"}), 400

	api_key = os.getenv("OPENWEATHER_API_KEY")

	try:
		if api_key:
			# Fetch live data from OpenWeatherMap (simple mapping)
			url = "http://api.openweathermap.org/data/2.5/weather"
			params = {"q": city, "appid": api_key, "units": "metric"}
			resp = requests.get(url, params=params, timeout=5)
			if resp.status_code != 200:
				# pass upstream body when available
				body = None
				try:
					body = resp.json()
				except Exception:
					body = resp.text
				return jsonify({"error": "failed to fetch from OpenWeather", "details": body}), 502

			data = resp.json()
			result = {
				"city": data.get("name"),
				"temp_c": data.get("main", {}).get("temp"),
				"description": (data.get("weather") or [{}])[0].get("description"),
				"source": "openweathermap"
			}
			return jsonify(result)

		# No API key -> return lightweight mock data
		key = city.lower()
		mock = {
			"london": {"temp_c": 10, "description": "light rain"},
			"paris": {"temp_c": 14, "description": "clear sky"},
			"new york": {"temp_c": 8, "description": "cloudy"},
		}
		res = mock.get(key, {"temp_c": 20, "description": "sunny (mock)"})
		return jsonify({"city": city.title(), **res, "source": "mock"})

	except requests.RequestException as e:
		return jsonify({"error": "upstream request failed", "details": str(e)}), 502
	except Exception as e:
		return jsonify({"error": "internal error", "details": str(e)}), 500


if __name__ == "__main__":
	port = int(os.getenv("PORT", 5000))
	# Don't require debug for basic deliverable; allow env override
	debug = os.getenv("FLASK_DEBUG", "False").lower() in ("1", "true", "yes")
	app.run(host="0.0.0.0", port=port, debug=debug)
