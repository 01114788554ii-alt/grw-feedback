import os
import base64
import requests
from urllib.parse import unquote
from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": True, "service": "grw-feedback"})


@app.route("/", methods=["POST"])
def upload():
    try:
        if not BOT_TOKEN or not CHAT_ID:
            return jsonify({"status": False, "error": "Missing BOT_TOKEN or CHAT_ID"}), 500

        base64_image = request.form.get("base64_image")
        caption = request.form.get("caption", "Screenshot")

        if not base64_image:
            return jsonify({"status": False, "error": "Missing image"}), 400

        decoded = unquote(base64_image)
        image_bytes = base64.b64decode(decoded)

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        files = {"photo": ("screenshot.jpg", image_bytes, "image/jpeg")}
        data = {
            "chat_id": CHAT_ID,
            "caption": unquote(caption),
            "parse_mode": "HTML"
        }

        response = requests.post(url, files=files, data=data, timeout=30)
        result = response.json()

        return jsonify({"status": result.get("ok", False), "result": result})

    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
