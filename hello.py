# _*_ coding: utf-8 _*_
from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

"""
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>欢迎来到flask的世界！你使用的浏览器是{}</h1>。'.format(user_agent)

@app.route('/user/<name>/')
def user(name):
    return '<h1>%s, Welcome!</h1>' % name
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
