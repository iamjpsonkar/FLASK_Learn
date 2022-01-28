from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello_world_f():
    return "<h1>Hello!!!</h1>"

@app.route("/fancy")
def fancy_f():
    return """
            <h1>Hello!!!</h1>
            <p>You are seeing a fancy hello</p>
            """
            
@app.route("/fancy_render")
def fancy_render_f():
    return render_template("first_page.html")
    

