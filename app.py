from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/languages')
def hello_languages():  # put application's code here
    return 'Hello Languages!'


@app.route('/skills')
def hello_skills():  # put application's code here
    return 'Hello Skills!'


@app.route('/experience')
def hello_experience():  # put application's code here
    return 'Hello Experience!'


@app.route('/education')
def hello_educations():  # put application's code here
    return 'Hello Education!'


@app.route('/hobbies')
def hello_hobbies():  # put application's code here
    return 'Hello Hobbies!'


if __name__ == '__main__':
    app.run()
