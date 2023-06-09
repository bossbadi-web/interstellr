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


@home.route('/booking', methods=['GET'])
def booking():
    return render_template('booking.html', tour=request.args.get('tour'))


@home.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@home.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


def setup(app):
    app.register_blueprint(home)
