from app import app

from flask import request
from flask import redirect
from flask import render_template


user_name = None


@app.route('/')
@app.route('/index')
def index():
    if user_name is None:
        return redirect('/login')

    user = {'nickname': user_name}

    html = render_template("hello.html", title='Welcome!', user=user)
    return html


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/do_login', methods=['POST'])
def do_login():
    global user_name
    user_name = request.form['login']

    if user_name:
        return redirect('/index')
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
