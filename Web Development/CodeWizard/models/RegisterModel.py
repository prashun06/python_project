import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:          # mongodb server setting
    def __int__(self):
        self.client = MongoClient()
        self.db = self.client.CodeWizerd
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())       # hashing the password in parameter

        id = self.Users.insert({"username": data.username,"email": data.email, "password": data.password })       # user information save in server
        print("uid is ", id)
        myuser = self.Users.find_one({"username": data.username})        # take the password from server using username

        if bcrypt.checkpw("avocado1".encode(), myuser["password"]):       # creat the password hash and matching the pass
            print("this matched")