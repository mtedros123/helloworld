from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Mikal Tedros! I am adding my first code change'
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/hello')
def hello():
    return render_template('hello.html')
if __name__ == '__main__':
    app.run()
