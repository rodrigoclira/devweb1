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

@app.route("/cookies")
def cookies():

    resp = make_response("Set cookies")

    cookies = request.cookies

    print(cookies)

    # resp.set_cookie(
    #     "flavor",
    #     value="chocolate chip",
    #     max_age=10,
    #     path=request.path
    # )

    resp.set_cookie("chocolate type", "dark")
    resp.set_cookie("chewy", "yes")
