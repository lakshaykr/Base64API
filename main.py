from flask import Flask, request, Response, Blueprint
import base64
from utils.keyvalidation import is_api_key_valid
from utils.usagemanager import update_use_count

bp = Blueprint('api', __name__)

@bp.route("/encode")
def encode():
    text = request.args.get("text")
    api_key = request.args.get("key")

    if not api_key:
        return Response("Missing 'key' parameter", status=400)
    if not is_api_key_valid(api_key):
        return Response("Invalid or locked API key", status=403)
    if not text:
        return Response("Missing 'text' parameter", status=400)

    result = update_use_count(api_key)
    if result["status"] == "error":
        return Response(result["message"], status=403)
    elif result["status"] == "limit_reached":
        return Response("API key limit reached (30 uses). Key is now locked.", status=429)


    encoded = base64.b64encode(text.encode()).decode()
    return Response(encoded, mimetype="text/plain")

