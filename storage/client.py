from pymongo import MongoClient


from dotenv import load_dotenv
import os

MONGO = os.getenv("MONGO_URI")

uri = f"{MONGO}"

client = MongoClient(uri)


db = client["database"]
users_collection = db["users"]

def get_user_by_id(user_id):
    return users_collection.find_one({"_id": user_id})


def create_new_user(user_id, api_key, use_count=0, last_use_hours_ago=0, inactivity_status=False, premium=False):
    post = {"_id":user_id, "api_key":api_key, "use_count":use_count, "last_use_hours_ago":last_use_hours_ago, "inactive":inactivity_status, "premium":premium}
    users_collection.insert_one(post)
    return "New Database Entry Created"

def get_api_key(user_id):
    user = users_collection.find_one({"_id": user_id})
    if user:
        return user.get("api_key")
    return None

def get_activity_status(user_id):
    user = users_collection.find_one({"_id": user_id})
    if user:
        return user.get("inactive")
    return None

def regenerate_api_key(user_id, new_api_key):
    result = users_collection.update_one(
        {"_id": user_id},
        {"$set": {"api_key": new_api_key}}
    )
    if result.matched_count:
        return "API key updated successfully"
    else:
        return "User not found"
