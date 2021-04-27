from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        print("Método POST")
        username = request.form['nm']
        resp = make_response(render_template('index.html', user = username))
        resp.set_cookie('user', username)
    elif request.method == 'GET':
        print("Método GET")
        username = request.cookies.get('user')
        resp = render_template('index.html', user = username)
        print(username)
    return resp
