from flask import render_template, Blueprint

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')


@home.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@home.route('/experience', methods=['GET'])
def experience():
    return render_template('experience.html')


@home.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@home.route('/spaceship', methods=['GET'])
def spaceship():
    return render_template('spaceship.html')


@home.route('/training', methods=['GET'])
def training():
    return render_template('training.html')


@home.route('/sources', methods=['GET'])
def sources():
    return render_template('sources.html')


def setup(app):
    app.register_blueprint(home)
