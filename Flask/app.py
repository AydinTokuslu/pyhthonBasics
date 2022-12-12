from flask import Flask, jsonify
from api.users import apiUsers
from api.product import apiProducts
from api.admin import apiAdmins


app = Flask(__name__)

# kayıt alanları
app.register_blueprint(apiUsers)
app.register_blueprint(apiProducts)
app.register_blueprint(apiAdmins)


@app.route("/")
def hello_world():
    return jsonify({"success": True, "message": "hello world!"})


@app.route("/shares")
def shares():
    # return "Shares Page"
    return jsonify({"success": True, "data": ["paylasim1", "paylasim2", "paylasim3"]})


@app.route("/profil")
def profil():
    return {"id": 1, "name": "Furkan", "age": 25, "following": 80, "followers": 100, "followersList": ["oguz", "alper"]}


if __name__ == "__main__":
    app.run(debug=True)
