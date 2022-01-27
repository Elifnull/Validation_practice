from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

class Dojos():
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, Now(), Now());"
        return MySQLConnection("dojo_survey").query_db(query,data)
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo["name"]) < 3:
            flash("Name must be more than 3 Characters.")
            is_valid = False
        if len(dojo["location"]) < 1:
            flash("Must Choose a Location.")
            is_valid = False
        if len(dojo["language"]) < 1:
            flash("Must choose a Language.")
            is_valid = False
        if len(dojo["comment"]) < 3:
            flash("Please leave a comment.")
            is_valid = False
        return is_valid