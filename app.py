from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def homepage(name=None):
    return render_template('index1.html', name=name)

@app.route('/hello')
def hello_page():
    return "Hello there"

@app.route('/user/<user>')
def user_page(user):
    return "User: {0}".format(user)

@app.route('/html/<page>')
def render_html(page):
    return render_template('{0}.html'.format(page))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
