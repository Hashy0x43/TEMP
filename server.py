
from flask import Flask, render_template, request
from geopy.geocoders import Nominatim

# I don't remember why I made this repo.

server = Flask(__name__)
geolocator = Nominatim(user_agent="Python3 on Linux")


@server.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        address = geolocator.geocode(request.form["address"])

        return render_template("index.html", address = address.raw)
    
    else:
        return render_template("index.html")


if __name__ == "__main__":
    server.run("127.0.0.1", 1984)


