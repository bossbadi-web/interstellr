from flask import render_template, Blueprint

about = Blueprint('about', __name__)


@about.route('/our-chapter', methods=['GET'])
def our_chapter():
    return render_template('about/our-chapter.html')


@about.route('/cte', methods=['GET'])
def cte():
    return render_template('about/cte.html')


@about.route('/legal', methods=['GET'])
def legal():
    return render_template('about/legal.html')


def setup(app):
    app.register_blueprint(about)
