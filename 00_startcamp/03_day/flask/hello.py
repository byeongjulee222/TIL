from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

    # 127.0.0.1 : local host address

@app.route('/ssafy')
def bye():
    return "This is ssafy !"