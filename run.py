import os
import json
from flask import Flask, render_template


app = Flask(__name__)


# routing
@app.route("/")
def index():  # this is a view
    return render_template("index.html")


@app.route("/about")
def about():
    # use data from server side and display on client side, add arguments
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # never in production deployment or when submitting!
    )
