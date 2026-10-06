from storage.client import users_collection



def update_use_count(api_key: str):
    record = users_collection.find_one({"api_key": api_key})
    
    if not record or record.get("locked", False):
        return {"status": "error", "message": "API key not found or locked"}

    new_count = record.get("use_count", 0) + 1

    users_collection.update_one(
        {"api_key": api_key},
        {"$set": {"use_count": new_count}}
    )

    if new_count >= 30:
        users_collection.update_one({"api_key": api_key}, {"$set": {"locked": True}})
        return {"status": "limit_reached", "use_count": new_count}

    return {"status": "ok", "use_count": new_count}
