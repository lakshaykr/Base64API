from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route("/encode")
def encode():
    text = request.args.get("text")
    if not text:
        return jsonify({"error": "Missing 'text' parameter"}), 400
    encoded = base64.b64encode(text.encode()).decode()
    return jsonify({encoded})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
