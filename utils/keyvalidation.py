from storage.client import users_collection

def is_api_key_valid(api_key):
    return users_collection.find_one({"api_key": api_key}) is not None
