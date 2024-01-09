from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def profile():
    return render_template("profile.html")

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/resume")
def resume():
    return render_template("resume.html")