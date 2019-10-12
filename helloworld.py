from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "hello world"

@app.route("/hello/")
def hello():
    return "hello world"

@app.route("/hello1/")
def hello1():
    return "hello1"

if __name__ == '__main__':
    app.run(port=8000, debug=True)