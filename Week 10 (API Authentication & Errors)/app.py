"""Small Flask app demonstrating improved API error handling.

Features:
- Custom ApiError exception with status code and optional payload
- Centralized JSON error handlers for ApiError, 400, 401, 404, 405, 500
- Simple API key auth via `X-API-KEY` header (env var API_KEY)
- Example endpoints:
  - GET / -> instructions
  - GET /divide?numerator=..&denominator=.. -> demonstrates validation and division errors
  - GET /secure -> demonstrates auth and returns 401 when missing/invalid

This file is intentionally small and self-contained for teaching error handling.
"""
from flask import Flask, request, jsonify
import os


class ApiError(Exception):
	"""Custom exception for API errors.

	Attributes:
		message: human-friendly message
		status_code: HTTP status code
		payload: additional data to include in the response
	"""

	def __init__(self, message, status_code=400, payload=None):
		super().__init__(message)
		self.message = message
		self.status_code = status_code
		self.payload = payload

	def to_dict(self):
		rv = {"message": self.message}
		if self.payload:
			rv["details"] = self.payload
		return rv


def make_error_response(message, status=400, details=None):
	body = {"error": {"message": message}}
	if details is not None:
		body["error"]["details"] = details
	return jsonify(body), status


app = Flask(__name__)


@app.errorhandler(ApiError)
def handle_api_error(err: ApiError):
	return jsonify({"error": err.to_dict()}), err.status_code


@app.errorhandler(400)
def handle_400(err):
	return make_error_response("Bad request", 400)


@app.errorhandler(401)
def handle_401(err):
	return make_error_response("Unauthorized", 401)


@app.errorhandler(404)
def handle_404(err):
	return make_error_response("Not found", 404)


@app.errorhandler(405)
def handle_405(err):
	return make_error_response("Method not allowed", 405)


@app.errorhandler(500)
def handle_500(err):
	# Avoid leaking internal details in production
	return make_error_response("Internal server error", 500)


def require_api_key():
	expected = os.getenv("API_KEY")
	if not expected:
		# No server-side API key configured; treat as auth disabled
		return True
	supplied = request.headers.get("X-API-KEY") or request.headers.get("Authorization")
	if not supplied:
		raise ApiError("Missing API key", status_code=401)
	# Support both raw key and Bearer token formats
	if supplied.startswith("Bearer "):
		supplied = supplied.split(" ", 1)[1]
	if supplied != expected:
		raise ApiError("Invalid API key", status_code=401)
	return True


@app.route("/")
def index():
	return jsonify({
		"app": "week-10-errors",
		"endpoints": ["GET /divide?numerator=..&denominator=..", "GET /secure (requires X-API-KEY header)"],
	})


@app.route("/divide")
def divide():
	# Simple input validation with informative errors
	num = request.args.get("numerator")
	den = request.args.get("denominator")
	if num is None or den is None:
		raise ApiError("Both 'numerator' and 'denominator' query parameters are required", status_code=400)

	try:
		n = float(num)
	except ValueError:
		raise ApiError("'numerator' must be a number", status_code=400, payload={"received": num})

	try:
		d = float(den)
	except ValueError:
		raise ApiError("'denominator' must be a number", status_code=400, payload={"received": den})

	if d == 0:
		raise ApiError("Division by zero is not allowed", status_code=400)

	result = n / d
	return jsonify({"numerator": n, "denominator": d, "result": result})


@app.route("/secure")
def secure():
	# Demonstrate auth + proper error handling
	require_api_key()
	return jsonify({"secret": "you have access"})


if __name__ == "__main__":
	port = int(os.getenv("PORT", 5000))
	debug = os.getenv("FLASK_DEBUG", "False").lower() in ("1", "true", "yes")
	app.run(host="0.0.0.0", port=port, debug=debug)
