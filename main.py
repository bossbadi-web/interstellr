import flask
import importlib
import os

app = flask.Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = os.getenv('secret_key')

for lib in os.listdir('routes'):
    if lib.endswith('.py'):
        module = importlib.import_module(f'routes.{lib[:-3]}')
        module.setup(app)
