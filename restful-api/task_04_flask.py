from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}

@app.route("/")
def home():
    """Əsas səhifə üçün endpoint."""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Sistemdəki bütün istifadəçi adlarının siyahısını qaytarır."""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """API-nin vəziyyətini yoxlayan endpoint."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Dinamik marşrut: Verilən istifadəçi adına görə məlumatları qaytarır."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Yeni istifadəçi əlavə edən endpoint."""
    # JSON-un düzgünlüyünü yoxlayırıq
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # Username olub-olmadığını yoxlayırıq
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    # İstifadəçinin artıq mövcud olub-olmadığını yoxlayırıq
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    # İstifadəçini lüğətə əlavə edirik
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    # Uğurlu cavab qaytarırıq (Status kodu: 201 Created)
    response = {
        "message": "User added",
        "user": users[username]
    }
    return jsonify(response), 201

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
