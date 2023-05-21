from flask import render_template, Blueprint

about = Blueprint('about', __name__)


@about.route('/contact', methods=['GET'])
def contact():
    return render_template('about/contact.html')


@about.route('/legal', methods=['GET'])
def legal():
    return render_template('about/legal.html')


def setup(app):
    app.register_blueprint(about)
