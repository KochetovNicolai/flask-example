from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/hello')
def hello():
    user = {'nickname': 'Dart Waider'}

    html = '''
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <h1>Hello, {}</h1>
      </body>
    </html>
    '''.format(user['nickname'])

    return html


from flask import render_template

@app.route('/hello_template')
def hello_template():
    user = {'nickname': 'Dart Waider'}

    # Jinja2
    html = render_template("hello.html", title='Welcome!', user=user)
    return html


@app.route('/dialog')
def dialog():
    user = {'nickname': 'Dart Waider'}

    replicas = [
        {
            'author': {'nickname': 'Dart Waider'},
            'body': 'Luke, I am Your Father.'
        },
        {
            'author': {'nickname': 'Luke'},
            'body': 'Noooooooooooo!'
        }
    ]

    html = render_template("dialog.html", user=user, replicas=replicas)
    return html


if __name__ == '__main__':
    app.run(debug=True)
