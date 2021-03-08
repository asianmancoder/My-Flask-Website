from flask import Flask, redirect, url_for, render_template
from reddit_memes import memes
app = Flask('app')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin')
def admin():
    return redirect(url_for("home"))


@app.route('/signin/<uid>')
def signin(uid):
    if uid == 'jlee, bilbobaggins':
        return "Welcome, Joseph!"
    else:
        return "You are not authorized to be here!"


@app.route("/info")
def info():
    return render_template('info.html')


@app.route('/memes')
def memes_page():
    return f'{memes()}'
