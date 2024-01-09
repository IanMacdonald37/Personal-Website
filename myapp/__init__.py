from flask import Flask, render_template, url_for

from pathlib import Path

from .routes import main

def create_app():

  app = Flask(__name__)
  app.instance_path = Path(".").resolve()
  app.register_blueprint(main)

  return app
