from app import app

from flask import render_template

import os


@app.route('/')
# @app.route('/<path>')
@app.route('/<path:path>')
def ls(path=None):

    if path is None or not os.path.isdir(path):
        path = '.'

    names = os.listdir(path)

    files = [{
        'name': name,
        'path': os.path.join(path, name),
        'is_dir': os.path.isdir(os.path.join(path, name))
    } for name in names]

    html = render_template("ls.html", title='Welcome!', files=files, path=path)

    return html


if __name__ == '__main__':
    app.run(debug=True)
