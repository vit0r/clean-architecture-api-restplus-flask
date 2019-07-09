"""Startup app liblaries
"""
from pathlib import Path

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

DB = SQLAlchemy()
MIGRATE = Migrate()


def register_blueprints(app):
    """Register blueprint auto by name BLUEPRINT_API"""
    bp_config = app.config['BLUEPRINTS']
    bp_version = bp_config.get('version')
    bp_prefix = bp_config.get('prefix')
    bp_dir = Path(app.root_path, bp_version)
    bp_files = bp_dir.glob('__init__.py')
    for bp_file in bp_files:
        bp_name = bp_file.name.replace('.py', '.BLUEPRINT_API')
        bp_mod = '.'.join([app.name, bp_version, bp_name])
        bp_module_name = import_string(bp_mod)
        app.register_blueprint(
            bp_module_name, url_prefix='{}{}'.format(bp_prefix, bp_version))
