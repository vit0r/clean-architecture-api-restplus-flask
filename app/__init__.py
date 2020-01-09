"""
APP flask init
"""

from core import DB, MIGRATE, get_instance, register_blueprints
from flask import Flask


def create_app():
    """Create app flask"""
    instance_path, environ_file = get_instance("v1")
    app = Flask(__name__, instance_path=instance_path)
    app.config.from_json(environ_file)
    app.url_map.strict_slashes = False
    DB.init_app(app)
    MIGRATE.init_app(app, DB)
    register_blueprints(app)
    return app
