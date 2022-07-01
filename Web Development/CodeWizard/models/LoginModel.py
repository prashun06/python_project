import pymongo, bcrypt
from pymongo import MongoClient


class LoginModel:
    def __int__(self):
        self.client = MongoClient()
        self.db = self.client.CodeWizerd
        self.Users = self.db.users

    def check_user(self, data):
        users = self.Users.find_one({"username": data.username})

        if users:
            if bcrypt.checkpw(data.password.encode(), users["password"]):
                return users
            else:
                return "error"
        else:
            return False

