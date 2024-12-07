import os
from flask import Flask, render_template


app = Flask(__name__)


# routing
@app.route("/")
def index(): # this is a view
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # never in production deployment or when submitting!
    )
