from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from pathlib import Path

app = Flask(__name__, static_folder="static", template_folder="templates")

# Chemins relatifs pour fonctionner partout (local + Render/Railway)
BASE_DIR = Path(__file__).parent
PULLS_FILE = BASE_DIR / "static" / "pulls.json"
QRCODES_DIR = BASE_DIR / "qrcodes"

def load_pulls():
    with open(PULLS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_pulls(pulls):
    with open(PULLS_FILE, "w", encoding="utf-8") as f:
        json.dump(pulls, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    pull_id = request.args.get("id")
    pulls = load_pulls()
    if pull_id:
        pull = next((p for p in pulls if p["id"] == pull_id), None)
        if not pull:
            return "Pull introuvable", 404
        return render_template("pull.html", pull=pull, all_pulls=pulls)
    # Classement
    sorted_pulls = sorted(pulls, key=lambda x: x["votes"], reverse=True)
    return render_template("leaderboard.html", pulls=sorted_pulls)

@app.route("/vote/<pull_id>", methods=["POST"])
def vote(pull_id):
    pulls = load_pulls()
    for p in pulls:
        if p["id"] == pull_id:
            p["votes"] += 1
            save_pulls(pulls)
            return jsonify({"success": True, "votes": p["votes"]})
    return jsonify({"success": False}), 404

@app.route("/qrcodes/<filename>")
def qrcode(filename):
    return send_from_directory(QRCODES_DIR, filename)

@app.route("/api/pulls")
def api_pulls():
    return jsonify(load_pulls())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
