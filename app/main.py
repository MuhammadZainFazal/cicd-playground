"""A small Flask web app that the pipeline tests, builds and deploys."""
import os

from flask import Flask, jsonify, request
import requests

from app import __version__
from app.calculator import add, divide, multiply, subtract

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(message="Hello from cicd-playground!", version=__version__)

    @app.get("/health")
    def health():
        # Used by Docker HEALTHCHECK and by deploy smoke tests.
        return jsonify(status="ok")

    @app.get("/calc/<op>")
    def calc(op):
        if op not in OPERATIONS:
            return jsonify(error=f"Unknown operation '{op}'"), 404
        try:
            a = float(request.args["a"])
            b = float(request.args["b"])
        except (KeyError, ValueError):
            return jsonify(error="Query params 'a' and 'b' must be numbers"), 400
        try:
            return jsonify(operation=op, result=OPERATIONS[op](a, b))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
