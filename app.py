from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('about_me.html')


@app.route('/languages')
def list_languages():  # put application's code here
    return render_template('languages.html')


@app.route('/experiences')
def list_experiences():  # put application's code here
    return render_template('experiences.html')


@app.route('/education')
def list_education():  # put application's code here
    return render_template('education.html')


@app.route('/skills')
def list_skills():  # put application's code here
    project = "hello Phuong"
    return render_template('skills.html', project=project)


@app.route('/interests')
def list_interests():  # put application's code here
    project = "hello Phuong"
    return render_template('interests.html', project=project)


@app.route('/projects')
def list_projects():
    # Greet the user
    return render_template('projects.html')


@app.route('/projects/<project>')
def show_project(project):
    # Greet the user
    return render_template('project.html', project=project)


if __name__ == '__main__':
    app.run()
