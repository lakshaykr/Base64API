from flask import Flask, request, Response
import base64
from utils.keyvalidation import is_api_key_valid

app = Flask(__name__)

@app.route("/encode")
def encode():
    text = request.args.get("text")
    api_key = request.args.get("key")

    if not api_key:
        return Response("Missing 'key' parameter", status=400)
    if not is_api_key_valid(api_key):
        return Response("Invalid or inactive API key", status=403)
    if not text:
        return Response("Missing 'text' parameter", status=400)

    encoded = base64.b64encode(text.encode()).decode()
    return Response(encoded, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
