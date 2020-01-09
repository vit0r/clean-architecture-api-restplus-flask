"""Libs for core apis
"""

from os import environ
from pathlib import Path

from .startup import DB, MIGRATE, register_blueprints

__all__ = ("environ", "Path", "DB", "MIGRATE", "register_blueprints", "get_instance")


def get_instance(app_version):
    """Get instance app by version"""
    app_dir = Path(__file__).parent
    instance_path = Path(app_dir / "instances")
    config_file = environ.get("ENVID", "develop_{}.json".format(app_version))
    environ_file = Path(instance_path / config_file)
    return str(instance_path), str(environ_file)
