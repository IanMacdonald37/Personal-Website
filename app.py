from flask import Flask, render_template, request, redirect, url_for, flash

from pathlib import Path

app = Flask(__name__)
app.instance_path = Path(".").resolve()