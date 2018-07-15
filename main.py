from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

@app.route('/ping')
def pong():
    return 'pong'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
