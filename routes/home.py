from flask import render_template, request, Blueprint

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')


@home.route('/experience', methods=['GET'])
def experience():
    return render_template('experience.html')


@home.route('/spaceship', methods=['GET'])
def spaceship():
    return render_template('spaceship.html')


@home.route('/training', methods=['GET'])
def training():
    return render_template('training.html')


@home.route('/register', methods=['GET'])
def register():
    return render_template('register.html', tour=request.args.get('tour'))


@home.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@home.route('/legal', methods=['GET'])
def legal():
    return render_template('legal.html')


def setup(app):
    app.register_blueprint(home)
