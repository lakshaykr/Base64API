from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route("/encode")
def encode():
    text = request.args.get("text")
    if not text:
        return Response("Missing 'text' parameter", status=400)

    encoded = base64.b64encode(text.encode()).decode()
    return Response(encoded, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
