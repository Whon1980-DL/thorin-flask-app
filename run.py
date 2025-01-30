import os
from flask import Flask, render_template

# creating an instance of Flask class and store it in variable called app with the first argument being the name of the applicaiton module - out package
app = Flask(__name__)

# this is a decorator and is a way of wrapping funciton. / indicate the root directory. When we try to browse the root directtory Flak will call the function index()
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # do not use debug=True in actual project
        debug=True)
