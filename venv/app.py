from flask import Flask, jsonify, request, abort

app = Flask(__name__)


PET_RECORDS = { # Mock Database
    "kitcat": 198,
    "petz1": 430
}

@app.route("/", methods=["GET"])
def root():
    return "Run Test"


@app.route("/status", methods=["POST"])
def status():
    
    if not request.is_json: # Check if request has JSON data
        abort(403, description = "JSON not in request")

    data = request.get_json()

    # Second Validator
    if "command" not in data or "practice_id" not in data:
        abort(403, description = "Missing 'command' or 'practice_id'")
    
    if data["command"] != "status": # Check that command is status
        abort(403, description='Invalid "command" value')

    id = str(data["practice_id"]).lower().strip() # Whitespace and upper-case handling
    pets_loaded = PET_RECORDS.get(id, 0)


    return jsonify({"pets_loaded_today": pets_loaded})

@app.route('/healtcheck', methods=['GET']) # check if API is working 
def healthcheck():
    return jsonify({"status": "working"})

@app.route("/practices/<practice_id>", methods=["GET"])
def get_practice(practice_id):
    pets_loaded = PET_RECORDS.get(practice_id, 0)
    return jsonify({"pets_loaded_today": pets_loaded})


@app.errorhandler(403)
def errorhandle(e):
    return jsonify({
        "error": "forbidden",
        "detail": getattr(e, "description", "Forbidden")
    }), 403


if __name__ == "__main__":
    app.run(debug=True, port=5000)
