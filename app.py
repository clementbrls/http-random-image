from flask import Flask, send_file, abort
import os
import json
import random

app = Flask(__name__)
DATA_DIR = os.environ.get("DATA_DIR", "/data")
CONFIG_FILE = os.path.join(DATA_DIR, "config.json")


def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            proba = float(config.get("proba_image_b", 0.25))
            return max(0.0, min(1.0, proba))
    except Exception:
        return 0.25


proba_b = load_config()
image_a_path = os.path.join(DATA_DIR, "a.webp")
image_b_path = os.path.join(DATA_DIR, "b.webp")

@app.route("/")
def serve_image():
    if not os.path.exists(image_a_path) or not os.path.exists(image_b_path):
        return abort(404, "Images manquantes")

    selected_image = image_b_path if random.random() < proba_b else image_a_path
    return send_file(selected_image, mimetype='image/webp')
