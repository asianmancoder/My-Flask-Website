from flask import Flask, redirect, url_for
import requests
import webbrowser

app = Flask('app')


@app.route('/')
def home():
    return '''
    <title>
    Home
</title>


<h1>
    Welcome to the homepage!
</h1>


<ul>
    <li>
        Hello
    </li>
    <li>
        World
    </li>
</ul>
    '''


@app.route('/admin')
def admin():
    return redirect(url_for("home"))


@app.route("/info")
def info():
    browser_open = webbrowser.open("https://flask-doc.readthedocs.io/en/latest/")

    return f'''<h1>
    Welcome to the information page!
</h1>

<h2>
    How was this website made?
</h2>

<ul>
    <li>
        I used Flask, a Python Web Framework
    </li>

    <li>
        It allows me to create a simple app (or website), and host it locally. I can then return HTML code from the functions in my program - This will become the source code of the website
    </li>

    <li>
        <a href="{browser_open}">Here</a> is some documentation for Flask
    </li>
</ul>
'''


if __name__ == "__main__":
    app.run()
    
