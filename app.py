from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello_world_f():
    return "<h1>Hello!!!</h1>"

@app.route("/fancy/")
def fancy_f():
    return """
            <h1>Hello!!!</h1>
            <p>You are seeing a fancy hello</p>
            """
            
@app.route("/fancy_render/")
def fancy_render_f():
    return render_template("first_page.html")

@app.route("/jinja_route/")
def jinja_route_f():
    return render_template("jinja_intro.html",name="Jay Prakash Sonkar",template_name="Jinja2")

@app.route('/jinja_expression/')
def jinja_expression_f():
    data=[]
    data.append({'name':'ajay','f_fruit':'orange','qty':1})
    data.append({'name':'ankit','f_fruit':'apple','qty':1.3})
    data.append({'name':'arun','f_fruit':'banana','qty':24})
    data.append({'name':'aman','f_fruit':'grapes','qty':2})
    data.append({'name':'abhay','f_fruit':'mango','qty':3})
    price={}
    price['orange']=70
    price['apple']=90
    price['banana']=2
    price['grapes']=40
    price['mango']=50
    return render_template('jinja_expression.html',data=data,price=price)
    
    

