from flask import Flask


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
@app.route('/hello')

def hello_world():
    return "Hello World!?!?!?!"

@app.route('/test/<search_query>')
def search_query(search_query):
    return search_query

@app.route('/test/<int:value>')
def search(value):
    print value + 100
    return "correct"

@app.route('/test/<float:value>')
def f_search(value):
    print value + 100
    return "correct"

@app.route('/test/<path:value>')
def p_search(value):
    print value
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == 'michael':
        return "Hello {}".format(name)
    else:
        return "Not Found", 404


if __name__ == '__main__':
    app.run()
