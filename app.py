from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests received"
)


@app.before_request
def count_requests():
    REQUEST_COUNT.inc()


@app.route("/")
def home():
    return jsonify({
        "message": "DevOps Lab 10 Application",
        "status": "running",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)