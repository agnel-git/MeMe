from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/play", methods=["POST"])
def play_note():
    note = request.json["note"]
    print(f"Play note: {note}")
    # You could trigger Pygame sound or logic here
    return jsonify({"status": "playing", "note": note})

if __name__ == "__main__":
    app.run(debug=True)
