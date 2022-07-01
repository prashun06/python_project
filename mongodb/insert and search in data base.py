
import pymongo
from pymongo import MongoClient


myClient= MongoClient()    # user = MongoClient.mydb.users  - all are command for accessing the data base
db= myClient.mydb
users=db.users
user1 = {"user": "Nick", "password" : "userpass", "favorit ": "shoes" }   # user information
user_id = users.insert_one(user1).inserted_id    # insert the information in data base
user_id    # show the id of user

user1 = {"user": "Prashun", "password" : "pastpass", "favorit ": "shoes" }
user2 = {"user": "Prashun", "password" : "pastpass", "favorit ": "shoes" }
user_id = users.insert_one(user2).inserted_id    # insert 2nd one


users = {{"one user data": "info"}, {"two user data": "info"}}    # multiple user data
Users = db.users
Inserted = Users.inserted_many(users)    # insert multiple user data in data base
Inserted.inserted_ids

# search from the data base
Users.find().count()   # count the total object or users
Users.find({"object": "info"}).count    # count that searched object

import datetime     # date and time field
#    date and time
current_date = datetime.datetime.now()
old_date = datetime.datetime(2009, 2, 2)
uid = Users.insert({"username": "abc", "date": current_date})   # insert in data base

# insert date of information  SERACH
Users.find({"date": {"$gte": old_date}}).count()   # $greater than equal ---the old date and count them
Users.find({"date": {"$lte": old_date}}).count()     # $less than equal
Users.find({"date": {"$exists": True}}).count()      # how many have input date
Users.find({"username": {"$ne": "name"}}).count()    # count how many have same username
           #  Field


# api.mongodb.com/python  - all api of mongodb
# search a username lot faster way with api
db.users.creat_index([("username", pymongo.ASCENDING)])   # searching index api