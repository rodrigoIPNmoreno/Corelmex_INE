from flask import Blueprint, request, jsonify

main = Blueprint('neural_blueprint', __name__)

@main.route('/')
def get_neural_network():
    return jsonify({"Response ": "Functional"})