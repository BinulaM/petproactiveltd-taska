from flask import Flask, jsonify, request, abort

app = Flask(__name__)


PET_RECORDS = {
    "kitcat": 198,
    "petz1": 430
}

@app.route("/", methods=["GET"])
def home():
    return "Flask Test"


@app.route("/status", methods=["POST"])
def status():
    
    if not request.is_json: # Check if request has JSON data
        abort(403)

    data = request.get_json()

    # Second Validator
    if "command" not in data or "practice_id" not in data:
        abort(403)
    
    if data["command"] != "status": # Check that command is status
        abort(403)

    id = data["practice_id"]
    pets_loaded = PET_RECORDS.get(id, 0)


    return jsonify({"pets_loaded_today": pets_loaded})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
