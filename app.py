from flask import Flask, jsonify, request

app = Flask(__name__)

# Health check (very important for Kubernetes)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200


# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask CI/CD App is running 🚀"
    })


# Sample API endpoint
@app.route("/api/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return jsonify({
        "message": f"Hello, {name}!"
    })


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)