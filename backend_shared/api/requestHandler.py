from backend_shared.database import db_connection, db_utils, db_executer
from backend_shared.security import verifier, token
from backend_shared.logger import logger
from backend_shared.utils import random
from backend_shared.types import BusinessResponse, BusinessError
from backend_shared.api import utils, cache
from flask import  send_from_directory

class RequestHandler:
    def __init__(self, config):
        self.config = config
        self.db_connection = db_connection.Connection(self.config["database"]["hostname"], self.config["database"]["user"]["username"], self.config["database"]["user"]["password"], self.config["database"]["name"], self.config["database"]["port"])
        self.verifier = verifier.Verifier(self.db_connection, self.config)
        self.db_executer = db_executer.Executer(self.db_connection, self.config)
        self.db_utils = db_utils.DBUtils()
        self.logger = logger.Logger()
        self.random = random.Random()
        self.tokenizer = token.Tokenizer(self.config)
        self.utils = utils.Utils(self.config)
        self.cache = cache.DataCache()

    def get_categories(self):
        categories = self.cache.get("categories")
        if categories: return BusinessResponse(self.random.CreateRandomId(), "categories", categories).toJson()
        categories = self.db_executer.get_categories()
        result = []
        for category in categories:
            result.append(self.db_utils.category_to_json(category))
        self.cache.add('categories', result)
        return BusinessResponse(self.random.CreateRandomId(), "categories", result).toJson()


    def get_sub_categories():pass
    def get_happy_ends():pass
    def get_combined():pass

    def limit_reached(self):
        return send_from_directory(self.utils.getThumbnailFolderPath(), f"limit-reached/limit-reached.png", as_attachment=True)
    def image_not_found(self):
        return send_from_directory(self.utils.getThumbnailFolderPath(), f"image-not-found/0.png", as_attachment=True)
    
    def get_image(self, request):
        id = "image-not-found"
        iid = 0
        try: id = self.verifier.escape_characters(request.args["id"])
        except: return self.image_not_found()
        try: iid = self.verifier.escape_characters(request.args["iid"])
        except: return self.image_not_found()
        return send_from_directory(self.utils.getThumbnailFolderPath(), f"{id}/{iid}.png", as_attachment=True)