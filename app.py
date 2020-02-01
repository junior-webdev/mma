from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def homepage(name=None):
    return render_template('index1.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
