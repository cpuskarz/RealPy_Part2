from flask import Flask

app = Flask(__name__)

@app.route('/')

@app.route('/hello')
def hello_world():
    return "Hi Chet"

if __name__ == '__main__':
    app.run()
