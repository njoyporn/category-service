from flask import Flask, request
from .requestHandler import RequestHandler
import os

api = Flask(__name__)

request_handler = None

base_route = "/api/v1"
data_path = f"{os.getcwd()}/binarys"

@api.route("/", methods=["GET"])
def index():
    return "200 OK from category-service"

@api.route(f"{base_route}/healthz", methods=["GET"])
def healthz():
    return "200 OK from category-service"

@api.route(f"{base_route}/categories", methods=["GET"])
def get_categories():
    return request_handler.get_categories()

@api.route(f"{base_route}/sub-categories", methods=["GET"])
def get_sub_categories():
    return ""

@api.route(f"{base_route}/happy-ends", methods=["GET"])
def get_happy_ends():
    return ""

@api.route(f"{base_route}/combined", methods=["GET"])
def get_Combined():
    return ""

@api.route(f"{base_route}/thumbnail", methods=["GET"])
def get_image():
    return request_handler.get_image(request)

def run(conf):
    global config, request_handler
    config = conf
    request_handler = RequestHandler(config)
    if config["category_service"]["cors_enabled"]:
        from flask_cors import CORS
        cors = CORS(api)
    api.run(debug=True, host=config["category_service"]["hostname"], port=config["category_service"]["port"])
