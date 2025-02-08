# Python has a built-in os module with methods for interacting with the operating system, like creating files and directories, 
# management of files and directories, input, output, environment variables, process management, etc.
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# creating an instance of Flask class and store it in variable called app with the first argument being the name of the applicaiton module - out package
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

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


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # the first memebr in the argument is the memebr.html and the second one is the member variable member = {} we created above
    return render_template("member.html", member=member)


# methods is added as argument in the route method as flask can only hanle get unless we specify post as well
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # can use either get method or square brakets. get throw non if key not present whereas [] throw exception.
        # print(request.form.get("name"))
        # print(request.form["email"])
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5002")),
        # do not use debug=True in actual project
        debug=True)
