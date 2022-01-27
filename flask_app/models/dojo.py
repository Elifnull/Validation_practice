from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

class Dojos():
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        