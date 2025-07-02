from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route("/encode")
def encode():
    text = request.args.get("text")
    if not text:
        return Response("Missing 'text' parameter", status=400)

    try:
        encoded = base64.b64encode(text.encode()).decode()
        return Response(encoded, mimetype="text/plain")
    except Exception as e:
        return Response(f"Encoding failed: {str(e)}", status=500)

@app.route("/decode")
def decode():
    encoded_text = request.args.get("text")
    if not encoded_text:
        return Response("Missing 'text' parameter", status=400)

    try:
        decoded = base64.b64decode(encoded_text.encode()).decode()
        return Response(decoded, mimetype="text/plain")
    except Exception as e:
        return Response(f"Decoding failed: {str(e)}", status=400)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
