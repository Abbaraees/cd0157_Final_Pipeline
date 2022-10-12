from flask import Flask, render_template

APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return render_template('index.html')



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
