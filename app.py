from flask import Flask, render_template, request, redirect, url_for, flash

from pathlib import Path

app = Flask(__name__)
app.instance_path = Path(".").resolve()

@app.route("/")
def profile():
    return render_template("profile.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")



if __name__ == "__main__":
    app.run()
