from flask import Flask

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
    

