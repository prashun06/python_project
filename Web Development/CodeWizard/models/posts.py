import pymongo, bcrypt
from pymongo import MongoClient
import humanize


class Posts:
    def __int__(self):
        self.client = MongoClient()
        self.db = self.client.CodeWizerd
        self.Users = self.db.users
        self.Posts = self.db.posts     # post in the javascript

    def insert_post(self, data):
        inserted = self.posts.insert({"username": data.username, "content": data.content})
        return True

    def get_all_posts(self):
        all_posts = self.Posts.find()
        new_posts = []

        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            post["timestamp"] = humanize.naturaltime(datatime.datetime.now() - post["data_added"])
            new_posts.append(post)


        return new_posts

