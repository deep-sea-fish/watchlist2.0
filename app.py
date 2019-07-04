from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return '欢迎来到我的观影列表'