from flask import send_from_directory, Blueprint

doc = Blueprint('doc', __name__)


@doc.route('/portfolio', methods=['GET'])
def portfolio():
    return send_from_directory('static', 'doc/portfolio.pdf')


def setup(app):
    app.register_blueprint(doc)
