import os
import json
from flask import Flask, render_template

# creating an instance of Flask class and store it in variable called app with the first argument being the name of the applicaiton module - out package
app = Flask(__name__)

# this is a decorator and is a way of wrapping funciton. / indicate the root directory. When we try to browse the root directtory Flak will call the function index()
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # doing with block to open json file "r" for read only and assigning the contents of the file to a new variable called json_data
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
        # do not use debug=True in actual project
        debug=True)
