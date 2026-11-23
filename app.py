from flask import Flask, jsonify, request

app = Flask(__name__)


# Basic home route
@app.route("/")
def home():
  return "<h1>Hello, World!</h1><p>Your Flask app is running.</p>"


# Simple JSON API endpoint
@app.route("/api/greet", methods=["GET"])
def greet():
  name = request.args.get("name", "Guest")
  return jsonify({"message": f"Hello, {name}!", "status": "success"})


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5000)
