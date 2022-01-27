from flask_app import app
from flask_app.models.dojo import Dojos
from flask import render_template, session, flash, request, redirect

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    if not Dojos.validate_dojo(request.form):
        return redirect('/')
    Dojos.save(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")
